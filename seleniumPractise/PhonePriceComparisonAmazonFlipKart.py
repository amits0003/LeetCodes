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
        phone_details.append((phone_name, price_val))

    return phone_details


# Function to get phone details from Flipkart
def get_flipkart_phones():
    driver.get("https://www.flipkart.com")
    search_input = driver.find_element(By.XPATH, "//input[@class='Pke_EE' and @name='q']")
    search_input.send_keys("iphone")
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)

    phone_details = []

    phones = driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
    prices = driver.find_elements(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']")

    for phone, price in zip(phones, prices):
        phone_name = phone.text
        price_text = price.text[1:]  # Skip the rupee symbol
        price_str_val = price_text.split(",")
        price_str = "".join(ele for ele in price_str_val)
        price_val = int(price_str)
        phone_details.append((phone_name, price_val))

    return phone_details


# Get phone details from both Amazon and Flipkart
amazon_phones = get_amazon_phones()
flipkart_phones = get_flipkart_phones()

# Create a DataFrame for the comparisons
comparison_data = []

for amazon_phone, amazon_price in amazon_phones:
    for flipkart_phone, flipkart_price in flipkart_phones:
        if amazon_phone.lower() in flipkart_phone.lower() or flipkart_phone.lower() in amazon_phone.lower():
            price_difference = flipkart_price - amazon_price
            comparison_data.append([amazon_phone, amazon_price, flipkart_phone, flipkart_price, price_difference])

# Convert the comparison data into a DataFrame
df = pd.DataFrame(comparison_data,
                  columns=['Amazon Phone', 'Amazon Price', 'Flipkart Phone', 'Flipkart Price', 'Price Difference'])

# Save the DataFrame to an Excel file
df.to_excel('phone_price_comparison.xlsx', index=False)

# Close the WebDriver
driver.quit()

print("Comparison data has been saved to phone_price_comparison.xlsx")
