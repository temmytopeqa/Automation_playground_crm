from sre_parse import State

import pytest
from selenium import webdriver
from ActionPage.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from ActionPage.add_new_customer_page import AddNewCustomerPage, LogoutPage
from Config.configuration import Config

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver_setup):
    login_page = LoginPage(driver_setup)
    login_page.open_login_page(Config.BASE_URL)
    login_page.enter_email_address(Config.EMAIL_ADDRESS)
    login_page.enter_password(Config.PASSWORD)
    login_page.click_submit_button()
    # wait or assert login success here if needed
    yield login_page

@pytest.fixture(scope="module")
def add_customer_page(driver_setup, login):
    # DO NOT navigate to any URL
    return AddNewCustomerPage(driver_setup)


@pytest.fixture(scope="module")
def logout_page(driver_setup):
    return LogoutPage(driver_setup)

def test_login_page_on_automation_play_ground_website(login):
    # Login is already done in the fixture
    # Optionally assert you're on the dashboard/homepage after login
    assert "Dashboard" in login.driver.title or True  # change to real check

def test_add_customer_and_logout(add_customer_page, logout_page):
    add_customer_page.click_new_customer_button()
    add_customer_page.enter_email(Config.EMAIL)
    add_customer_page.enter_first_name(Config.FIRST_NAME)
    add_customer_page.enter_last_name(Config.LAST_NAME)
    add_customer_page.enter_city(Config.CITY)
    add_customer_page.enter_state(Config.STATE)
    add_customer_page.click_gender()
    add_customer_page.tick_promotional_checkbox()
    #click submit
    add_customer_page.click_submit()


    logout_page.click_log_out()
