# from pykafka import KafkaClient
#
# client = KafkaClient(hosts='localhost:9092')
#
# producer = client.topics['mytopic'].get_producer()
# producer.produce('my message')
#
# consumer = client.topics['mytopic'].get_balanced_consumer(consumer_group='mygroup')
# message = consumer.consume()
#
# print(message.value)
from confluent_kafka import Consumer
import pandas as pd

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup'})
c.subscribe(['mytopic'])

data = []

for i in range(1000):
    msg = c.poll(1.0)
    if msg is not None:
        data.append(msg.value())

df = pd.DataFrame(data)
print(df.describe())
