from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the browser (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.geeksforgeeks.org/python-programming-language/')

# Extract content after the JavaScript has rendered the page
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

# Perform the extraction as before
headlines = soup.find_all('h2', class_='headline')
for headline in headlines:
    print(headline.text)

# Close the browser
driver.quit()
