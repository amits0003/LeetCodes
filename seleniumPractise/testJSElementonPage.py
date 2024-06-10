from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()  # Or specify the path to your chromedriver

# Navigate to the Alodokter website
driver.get("https://www.alodokter.com/")

try:
    # Wait for the search input to be visible and enabled
    search_input = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.ID, "searchinput"))
    )

    # Type a search query into the input
    search_input.send_keys("heart disease")
    search_input.send_keys(Keys.RETURN)  # Simulate pressing Enter

    # You can also get the value of the search input if needed
    input_value = search_input.get_attribute("value")
    print("Input value:", input_value)

    # Alternatively, you can locate the search input by XPath or CSS Selector
    # using the form's ID 'searchbar'
    # search_input = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//form[@id='searchbar']//input[@type='text']"))
    # )
    # search_input.send_keys("heart disease")
    # search_input.send_keys(Keys.RETURN)

finally:
    # Close the browser
    driver.quit()
