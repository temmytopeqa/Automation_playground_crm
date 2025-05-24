from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from LocatorPage.login_locator import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.EMAIL_ADDRESS)
        )
        enter_email_address.send_keys(email_address)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.PASSWORD)
        )
        enter_password.send_keys(password)

    def click_submit_button(self):
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON)
        )
        submit_button.click()


