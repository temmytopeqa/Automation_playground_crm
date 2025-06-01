import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, ElementNotInteractableException

from LocatorPage.add_new_customer_locator import AddNewCustomerLocators, LogoutLocators

DEFAULT_SLEEP_TIME = 0.5

class AddNewCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_customer_button(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.NEW_CUSTOMER_BUTTON)
        )
        btn.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_email(self, email):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.EMAIL)
        )
        field.clear()
        field.send_keys(email)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_first_name(self, first_name):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.FIRST_NAME)
        )
        field.clear()
        field.send_keys(first_name)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_last_name(self, last_name):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.LAST_NAME)
        )
        field.clear()
        field.send_keys(last_name)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_city(self, city):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.CITY)
        )
        field.clear()
        field.send_keys(city)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_state(self, state):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.STATE)
        )
        field.clear()
        field.send_keys(state)
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_gender(self):
        gender_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.GENDER)
        )
        gender_btn.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def tick_promotional_checkbox(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.PROMO_CHECKBOX)
        )
        checkbox.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_submit(self):
        submit_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.SUBMIT_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(1)

        try:
            submit_btn.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            ActionChains(self.driver).move_to_element(submit_btn).click().perform()

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_log_out(self):
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LogoutLocators.LOG_OUT)
        )
        logout_btn.click()
        time.sleep(0.5)
