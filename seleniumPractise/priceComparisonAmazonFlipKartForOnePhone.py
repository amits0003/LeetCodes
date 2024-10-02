from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
search_input = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_input.send_keys("iphone 15 pro max")
search_input.send_keys(Keys.RETURN)
phone_name_on_amazon = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']").text
price_text = driver.find_element(By.CSS_SELECTOR, ".a-price-whole").text

price_str_val = price_text.split(",")

price_str1 = "".join(ele for ele in price_str_val)
iphonePriceAmazon = int(price_str1)

driver.get("https://www.flipkart.com")
search_input = driver.find_element(By.XPATH, "//input[@class='Pke_EE' and @name='q']")

search_input.send_keys("iphone 15 pro max")
search_input.send_keys(Keys.RETURN)

phone_name_on_flipkart = driver.find_element(By.XPATH, "//div[@class='KzDlHZ']").text

price_text2 = driver.find_element(By.XPATH, "//div[@class='Nx9bqj _4b5DiR']").text

price_str_val2 = price_text2.split(",")

price_str2 = "".join(ele for ele in price_str_val2)
flipkartPriceAmazon = int(price_str2[1:])
if phone_name_on_flipkart.lower().__contains__("iphone 15 pro max") and phone_name_on_amazon.lower().__contains__(
        "iphone 15 pro max"):
    print("phones are same")

    if flipkartPriceAmazon == iphonePriceAmazon:
        print("prices of iphone 15 pro max are equal on both portals")
    elif flipkartPriceAmazon > iphonePriceAmazon:
        print("Price of iphone 15 pro max at flipkart is more than price of iphone 15 pro max on amazon "
              "and the difference is : ", flipkartPriceAmazon - iphonePriceAmazon)
    elif flipkartPriceAmazon < iphonePriceAmazon:
        print("Price of iphone 15 pro max at amazon is more than price of iphone 15 pro max on flipkart "
              "and the difference is : ", iphonePriceAmazon - flipkartPriceAmazon)
else:
    print("phone compared for prices are different, skipping the comparison")
