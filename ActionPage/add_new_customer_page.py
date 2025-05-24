from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from LocatorPage.add_new_customer_locator import AddNewCustomerLocators, LogoutLocators

DEFAULT_SLEEP_TIME = 1

class AddNewCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_customer_button(self):
        btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.NEW_CUSTOMER_BUTTON)
        )
        btn.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.EMAIL)
        )
        email_field.send_keys(email)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_first_name(self, first_name):
        first_name_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.FIRST_NAME)
        )
        first_name_field.send_keys(first_name)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_last_name(self, last_name):
        last_name_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.LAST_NAME)
        )
        last_name_field.send_keys(last_name)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_city(self, city):
        city_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.CITY)
        )
        city_field.send_keys(city)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_state(self, state):
        state_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.STATE)
        )
        state_field.send_keys(state)
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_gender(self):
        gender_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.GENDER)
        )
        gender_btn.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_add_to_promotional_list(self):
        promo_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddNewCustomerLocators.ADD_TO_PROMOTIONAL_LIST)
        )
        promo_checkbox.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_submit_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddNewCustomerLocators.SUBMIT_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        try:
            element.click()
        except:
            ActionChains(self.driver).move_to_element(element).click().perform()


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_log_out(self):
        logout_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutLocators.LOG_OUT)
        )
        logout_btn.click()
        time.sleep(DEFAULT_SLEEP_TIME)
