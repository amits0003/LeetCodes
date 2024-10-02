import re
import time
import logging as log
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pandas as pd

amazon_collection = []
flipkart_collection = []
amazon_rating_collection = []
flipkart_rating_collection = []
pages = 4


def AmazonSearchResult():
    driver = webdriver.Chrome()

    driver.get("https://www.amazon.in/")

    # Hit the Search Bar
    search_input = driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
    search_input.send_keys("laptop")
    search_input.send_keys(Keys.RETURN)
    # laptop_rating_coll = driver.find_element(By.XPATH, "i span.a-icon-alt").text

    time.sleep(5)
    # Get the Search Results
    for _ in range(pages):
        laptop_name_collection1 = driver.find_elements(By.CSS_SELECTOR, "h2 a span")
        laptop_price_collection1 = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
        laptop_rating_coll1 = driver.find_elements(By.CSS_SELECTOR, "i span.a-icon-alt")

        # collection1 = []
        for each_laptop_name, each_laptop_price, each_laptop_rating in zip(laptop_name_collection1,
                                                                           laptop_price_collection1,
                                                                           laptop_rating_coll1):
            priceTmp = each_laptop_price.text.split(",")
            if each_laptop_name.text != '' or priceTmp != ['']:
                rPriceVal = int("".join(ele for ele in priceTmp))
                # data = {each_laptop_name.text : rPriceVal }
                data = {
                    "name": each_laptop_name.text,
                    "price": rPriceVal,
                    "rating": each_laptop_rating.text
                }
                amazon_collection.append(data)

        try:
            next_button = driver.find_element(By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator' and text()='Next']")
            next_button.click()
        except Exception as e:
            log.info(e)

    driver.quit()


def FlipkartSearchResult():
    driver = webdriver.Chrome()

    driver.get("https://www.flipkart.com/")

    # Hit the Search Bar
    search_input = driver.find_element(By.XPATH, "//input[@class='Pke_EE' and @name='q']")
    search_input.send_keys("laptop")
    search_input.send_keys(Keys.RETURN)
    # laptop_rating_coll = driver.find_element(By.XPATH, "i span.a-icon-alt").text
    time.sleep(5)

    # collection2 = []

    for _ in range(pages):

        # Get the Search Results
        laptop_name_collection1 = driver.find_elements(By.CSS_SELECTOR, ".KzDlHZ")
        laptop_price_collection1 = driver.find_elements(By.XPATH, "//div[@class='Nx9bqj _4b5DiR']")
        laptop_rating_coll1 = driver.find_elements(By.CSS_SELECTOR, ".XQDdHH")

        for each_laptop_name, each_laptop_price, each_laptop_rating in zip(laptop_name_collection1,
                                                                           laptop_price_collection1,
                                                                           laptop_rating_coll1):
            try:
                priceTmp = each_laptop_price.text.split(",")
                priceTmp1 = "".join(ele for ele in priceTmp)
                if each_laptop_name.text != '' or priceTmp != ['']:
                    rPriceVal = int(priceTmp1[1:])
                    data = {
                        "name": each_laptop_name.text,
                        "price": rPriceVal,
                        "rating": each_laptop_rating.text
                    }
                    flipkart_collection.append(data)
            except StaleElementReferenceException:
                continue

        try:
            next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
            next_button.click()
        except Exception as e:
            log.info(e)

    driver.quit()


AmazonSearchResult()
FlipkartSearchResult()

print("data scrapping done for both amazon and flipkart")


def normalise_list(name):
    return re.sub(r'\W+', ' ', name).strip().lower()


def get_brand_name(laptop_name):
    """check the laptops brand name, to check if they are from the same brand"""
    return laptop_name.split()[0].lower()


def best_match_pattern(laptop_name, laptop_List):
    lap_name = normalise_list(laptop_name)
    brand_name = get_brand_name(lap_name)
    best_match = None
    best_score = 0
    for each_laptop_name in laptop_List:
        # for lname in each_laptop_name.keys():
        lname = each_laptop_name["name"]
        if get_brand_name(normalise_list(lname)) == brand_name:
            normalized_laptop_list_name = normalise_list(lname)
            match_score = len(set(lap_name.split()) & set(normalized_laptop_list_name.split()))
            if match_score > best_score:
                best_match = each_laptop_name
                best_score = match_score

    return best_match


comparison_data = []

# Data Comparison
# for amazon_laptop_details in amazon_collection:
#     for am_lp_name, amazon_laptop_price in amazon_laptop_details.items():
#         best_match = best_match_pattern(am_lp_name, flipkart_collection)
#         if best_match:
#             flipkart_name, flipkart_price = best_match
#             price_difference = amazon_laptop_price - flipkart_price
#             if price_difference < 0:
#                 price_difference = price_difference * -1
#             comparison_data.append([am_lp_name, amazon_laptop_price, flipkart_name, flipkart_price, price_difference])

# Data Comparison Part 2 :
for amazon_laptops_details in amazon_collection:
    amazon_laptop_name = amazon_laptops_details['name']
    amazon_laptop_price = amazon_laptops_details['price']
    amazon_laptop_rating = amazon_laptops_details['price']
    best_match = best_match_pattern(amazon_laptop_name, flipkart_collection)
    if best_match:
        flipkart_laptop_name = best_match['name']
        flipkart_laptop_price = best_match['price']
        flipkart_laptop_rating = best_match['rating']
        price_diff = abs(amazon_laptop_price - flipkart_laptop_price)
        comparison_data.append(
            [amazon_laptop_name, amazon_laptop_price, amazon_laptop_rating, flipkart_laptop_name, flipkart_laptop_price,
             flipkart_laptop_rating, price_diff])

wb = pd.DataFrame(comparison_data, columns=["Amazon Laptop Name", "Amazon Laptop Price", "Amazon Laptop Rating",
                                            "Flipkart Laptop Name", "Flipkart Laptop Price", "Flipkart Laptop Rating",
                                            "Laptop Price Difference"])

wb.to_excel("Laptop_Comparison_DataUpto4Pages.xlsx", index=False)

print("Comparison data has been written to the sheet Laptop_Comparison_Data1.xlsx")
