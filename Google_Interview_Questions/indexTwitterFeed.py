import tweepy
import psycopg2
from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
import logging

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Database credentials
DB_NAME = 'your_db_name'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'
DB_HOST = 'localhost'

# Twitter Service to interact with the API
class TwitterService:
    def __init__(self):
        auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def fetch_user_feed(self, count=100):
        """
        Fetch user's home timeline feed.
        :param count: Number of tweets to fetch
        :return: List of tweets
        """
        try:
            tweets = self.api.home_timeline(count=count)
            return tweets
        except Exception as e:
            logging.error(f"Error fetching tweets: {e}")
            return []

# Database Service for storing and querying data
class DatabaseService:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
        )
        self.create_table()

    def create_table(self):
        """Create the tweets table if not exists."""
        query = """
        CREATE TABLE IF NOT EXISTS tweets (
            id BIGINT PRIMARY KEY,
            text TEXT,
            created_at TIMESTAMP,
            user_name VARCHAR(100),
            screen_name VARCHAR(100)
        );
        """
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()

    def save_tweet(self, tweet):
        """Save a tweet into the database."""
        query = """
        INSERT INTO tweets (id, text, created_at, user_name, screen_name)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (
                tweet.id, tweet.text, tweet.created_at, tweet.user.name, tweet.user.screen_name
            ))
            self.conn.commit()

    def fetch_all_tweets(self):
        """Fetch all tweets from the database."""
        query = "SELECT * FROM tweets ORDER BY created_at DESC;"
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

# Flask API for querying and managing feed
app = Flask(__name__)
db_service = DatabaseService()
twitter_service = TwitterService()

@app.route('/api/tweets', methods=['GET'])
def get_tweets():
    """
    API to get the indexed tweets.
    """
    tweets = db_service.fetch_all_tweets()
    return jsonify(tweets)

@app.route('/api/fetch', methods=['POST'])
def fetch_and_index_tweets():
    """
    API to manually trigger fetching of tweets and indexing them in the database.
    """
    tweets = twitter_service.fetch_user_feed(count=100)
    for tweet in tweets:
        db_service.save_tweet(tweet)
    return jsonify({"message": "Tweets indexed successfully!"})

# Scheduler for periodic fetching and indexing of tweets
scheduler = BackgroundScheduler()

def fetch_and_index_periodically():
    tweets = twitter_service.fetch_user_feed(count=100)
    for tweet in tweets:
        db_service.save_tweet(tweet)
    logging.info("Fetched and indexed new tweets.")

scheduler.add_job(fetch_and_index_periodically, 'interval', minutes=10)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
