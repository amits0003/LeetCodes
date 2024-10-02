import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Initialize the WebDriver
driver = webdriver.Chrome()


# Function to get phone details from Amazon
def get_amazon_phones():
    driver.get("https://www.amazon.in/")
    search_input = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search_input.send_keys("iphone")
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)

    phone_details = []

    phones = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    prices = driver.find_elements(By.CSS_SELECTOR, ".a-price-whole")

    for phone, price in zip(phones, prices):
        phone_name = phone.text
        price_text = price.text
        price_str_val = price_text.split(",")
        price_str = "".join(ele for ele in price_str_val)
        price_val = int(price_str)
        phone_details.append({phone_name: price_val})

    return phone_details


# Function to get phone details from Flipkart
def get_flipkart_phones():
    driver.get("https://www.flipkart.com")
    search_input = driver.find_element(By.XPATH, "//input[@class='Pke_EE' and @name='q']")
    search_input.send_keys("iphone")
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)

    phone_details = []

    phones = driver.find_elements(By.XPATH, "//div[@class='KzDlHZ']")
    prices = driver.find_elements(By.XPATH, "//div[@class='Nx9bqj _4b5DiR']")

    for phone, price in zip(phones, prices):
        phone_name = phone.text
        price_text = price.text[1:]  # Skip the rupee symbol
        price_str_val = price_text.split(",")
        price_str = "".join(ele for ele in price_str_val)
        price_val = int(price_str)
        phone_details.append({phone_name: price_val})

    return phone_details


# Get phone details from both Amazon and Flipkart
amazon_phones = get_amazon_phones()
flipkart_phones = get_flipkart_phones()

# Create a DataFrame for the comparisons
comparison_data = []


# Normalize phone names for better comparison
def normalize_name(name):
    return re.sub(r'\W+', ' ', name).strip().lower()


# Function to find the best match for a phone name in a list of phones
def find_best_match(phone_name, phone_list):
    normalized_name = normalize_name(phone_name)
    best_match = None
    best_match_score = 0
    for phone in phone_list:
        for name in phone.keys():
            normalized_list_name = normalize_name(name)
            # Calculate a simple match score based on common substrings
            match_score = len(set(normalized_name.split()) & set(normalized_list_name.split()))
            if match_score > best_match_score:
                best_match = (name, phone[name])
                best_match_score = match_score
    return best_match


for amazon_phone in amazon_phones:
    for amazon_name, amazon_price in amazon_phone.items():
        best_match = find_best_match(amazon_name, flipkart_phones)
        if best_match:
            flipkart_name, flipkart_price = best_match
            price_difference = flipkart_price - amazon_price
            if price_difference < 0:
                price_difference = price_difference * -1
            comparison_data.append([amazon_name, amazon_price, flipkart_name, flipkart_price, price_difference])

# Convert the comparison data into a DataFrame
df = pd.DataFrame(comparison_data,
                  columns=['Amazon Phone', 'Amazon Price', 'Flipkart Phone', 'Flipkart Price', 'Price Difference'])

# Save the DataFrame to an Excel file
df.to_excel('phone_price_comparison.xlsx', index=False)

print("Comparison data has been saved to phone_price_comparison.xlsx")
