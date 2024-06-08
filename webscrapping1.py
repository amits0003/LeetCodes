import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send an HTTP request
url = 'https://www.geeksforgeeks.org/python-programming-language/'
response = requests.get(url)
global soup
# Step 2: Parse the HTML content
if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    #print(soup.prettify())
    s = soup.find('div', class_='darkMode-wrap')
    content = s.find_all('button')

    print(content)
else:
    print('Failed to retrieve the webpage')

# Step 3: Extract data
headlines = soup.find_all('h2', class_='headline')


# Step 4: Store the data in a CSV file
with open('headlines.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])

    for headline in headlines:
        writer.writerow([headline.text])
