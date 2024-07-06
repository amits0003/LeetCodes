# importing necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By


# for holding the resultant list
element_list = []

driver = webdriver.Chrome()
page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="
driver.get(page_url)
title = driver.find_elements(By.CLASS_NAME, "title")
price = driver.find_elements(By.CLASS_NAME, "price")
description = driver.find_elements(By.CLASS_NAME, "description")
rating = driver.find_elements(By.CLASS_NAME, "ratings")

for i in range(len(title)):
    element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(element_list)

# closing the driver
driver.close()
