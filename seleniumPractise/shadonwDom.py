from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Navigate to the page containing the shadow root
driver.get('https://www.alodokter.com/')

# Step 3: Execute JavaScript to access the shadow DOM and find the target element
shadow_host = driver.find_element(By.CSS_SELECTOR, '#shadow-root')

# Step 4: Define a JavaScript script to access the shadow root and query the element within it
script = """
return arguments[0].shadowRoot.querySelector('.target');
"""

# Step 5: Execute the script and get the element
target_element = driver.execute_script(script, shadow_host)

# Perform actions on the target element, e.g., click or extract text
if target_element:
    print("Element found:", target_element.text)
else:
    print("Element not found")

# Step 6: Close the WebDriver
driver.quit()
