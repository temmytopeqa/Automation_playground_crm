from selenium.webdriver.common.by import By

class HomeLocators:
    ADD_CUSTOMER_BUTTON = (By.ID, "add-customer")

class AddNewCustomerLocators:

    NEW_CUSTOMER_BUTTON = (By.ID, "new-customer")
    EMAIL = (By.ID, "EmailAddress")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    CITY = (By.ID, "City")
    STATE = (By.ID, "StateOrRegion")
    GENDER = (By.CSS_SELECTOR, "input[name='gender'][value='male']")
    PROMO_CHECKBOX = (By.NAME, "promos-name")
    SUBMIT_BUTTON =  (By.XPATH, "//button[@type='submit']")

class LogoutLocators:
    LOG_OUT = (By.CLASS_NAME, "nav-link")
