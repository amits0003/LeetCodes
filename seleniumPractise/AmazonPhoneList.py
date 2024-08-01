import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.set_window_size(500, 400)
driver.get("https://www.amazon.in/")

search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                           "//input[@id='twotabsearchtextbox']")))

search_input.send_keys("iphone")
search_input.send_keys(Keys.RETURN)
pr = driver.find_element(By.XPATH, "//span[@class='a-size-base s-underline-text']").text

# Step 5: Extract search results
phone_names = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
phone_prices = driver.find_elements(By.CSS_SELECTOR, ".a-price-whole")
phone_ratings = driver.find_elements(By.XPATH, "//span[@class='a-size-base s-underline-text']")
#a div span.a-declarative a i span.a-icon-alt

# Step 6: Store results in a structured format
data = []
for name, price, rating in zip(phone_names, phone_prices, phone_ratings):
    data.append({
        "Phone Name": name.text,
        "Price": price.text,
        "Rating": rating.text
    })

# Convert to a DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("amazon_iphone_search_results.xlsx", index=False)

print("Search results saved to amazon_iphone_search_results.xlsx")

driver.quit()
