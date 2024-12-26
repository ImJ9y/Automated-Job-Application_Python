from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "YOUR ACCOUNT"
ACCOUNT_PASSWORD = "YOUR PASSWORD!"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get('COPY THE URL AFTER YOU FILTER')

    sign_up = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    sign_up.click()

except:
    print("Signing out - retry it")
    driver.quit()

time.sleep(3)

user_id = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
user_id.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("Called")
    listing.click()
    time.sleep(2)

    try:
        easyApply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
        easyApply_button.click()

        submit_button = driver.find_element(By.CSS_SELECTOR, value="footer button")

        if submit_button.get_attribute("aria-label") == "Submit application":
            submit_button.click()

            done_button = driver.find_element(By.CLASS_NAME, value='artdeco-button artdeco-button--2 artdeco-button--primary ember-view mlA block')
            done_button.click()

        elif submit_button.get_attribute("aria-label") == "Continue to next step":
            submit_button.click()

            if submit_button.get_attribute("aria-label") == "Review your application":
                review_button = driver.find_element(By.XPATH, "//button[@aria-label='Review your application']")
                review_button.click()

                apply_button = driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
                apply_button.click()

                done_button = driver.find_element(By.CLASS_NAME, value='artdeco-button artdeco-button--2 artdeco-button--primary ember-view mlA block')
                done_button.click()

            else:
                close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_element(By.XPATH, value="//button[span[text()='Discard']]")
                discard_button.click()
                print("Complex application, skipped.")
                continue

        else:
            close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.XPATH, value="//button[span[text()='Discard']]")
            discard_button.click()
            print("Complex application, skipped.")
            continue

    except NoSuchElementException:
        print("No Application button, skipped.")
        continue

driver.quit()
