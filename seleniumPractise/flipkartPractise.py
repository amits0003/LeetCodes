import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to Flipkart
    driver.get("https://www.flipkart.com")

    # Step 2: Close the login pop-up if it appears
    # try:
    #     close_login_popup = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    #     )
    #     close_login_popup.click()
    # except Exception as e:
    #     print("No login pop-up found or failed to close it.", e)

    # Step 3: Search for "iPhone"
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("iPhone")
    search_bar.send_keys(Keys.RETURN)

    # Step 4: Wait for the results to be displayed
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._1YokD2._3Mn1Gg")))

    # Step 5: Extract search results
    phone_names = driver.find_elements(By.CSS_SELECTOR, ".KzDlHZ")
    phone_prices = driver.find_elements(By.CSS_SELECTOR, "._4b5DiR")
    phone_ratings = driver.find_elements(By.CSS_SELECTOR, ".XQDdHH")

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
    df.to_excel("flipkart_iphone_search_results.xlsx", index=False)

    print("Search results saved to flipkart_iphone_search_results.xlsx")

finally:
    # Close the WebDriver
    driver.quit()
