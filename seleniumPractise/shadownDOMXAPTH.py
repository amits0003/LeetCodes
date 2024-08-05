from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.alodokter.com/")


host_element = driver.find_element(By.XPATH, '//*[@id="top-navbar-view"]')

# Use JavaScript to access the shadow root
search_input = driver.execute_script('return arguments[0].shadowRoot.querySelector("#searchinput")', host_element)

search_input.send_keys("Hello")

search_input.send_keys(Keys.ENTER)

driver.quit()