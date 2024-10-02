from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# LinkedIn Credentials
username = "amitk.work03@gmail.com"
password = "Rockey@123"

# Initialize WebDriver
# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()


def login_to_linkedin(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # Enter email
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(username)

    # Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    # Click login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)


def search_jobs(driver):
    # Open jobs section
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(3)

    # Search for Senior Python Developer in Noida
    search_box = driver.find_element(By.XPATH, "//input[contains(@class, 'jobs-search-box__text-input')]")
    search_box.send_keys("Senior Python Developer")
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)

    # Add location (Noida)
    location_box = driver.find_element(By.XPATH, "//input[@autocomplete='address-level2' and @type='text']")
    location_box.clear()
    location_box.send_keys("Noida")
    time.sleep(1)
    location_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Filter by posted in last 24 hours
    driver.find_element(By.XPATH, "//*/button[@id='searchFilter_timePostedRange']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[contains(., 'Past 24 hours')]").click()
    time.sleep(2)


def apply_to_jobs(driver):
    applied_jobs = []

    jobs = driver.find_elements(By.XPATH, "//ul[@class='jobs-search-results__list']//li")
    for job in jobs:
        job_title = job.find_element(By.CSS_SELECTOR, ".job-card-list__title").text

        # Check if job has already been applied
        if job_title not in applied_jobs:
            job.click()
            time.sleep(2)

            try:
                # Check if the "Easy Apply" button is available
                apply_button = driver.find_element(By.XPATH, "//button[contains(., 'Easy Apply')]")
                apply_button.click()
                time.sleep(1)

                # Submit application (if no further inputs are required)
                submit_button = driver.find_element(By.XPATH, "//button[contains(., 'Submit application')]")
                submit_button.click()
                print(f"Applied to {job_title}")

                # Mark job as applied
                applied_jobs.append(job_title)
                time.sleep(2)
            except:
                print(f"Could not apply to {job_title}, skipping.")
            time.sleep(3)


# Run the automation
login_to_linkedin(driver, username, password)
search_jobs(driver)
apply_to_jobs(driver)

# Close the browser
driver.quit()
