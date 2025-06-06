from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.firstname = (By.ID, "first-name")
        self.lastname = (By.ID, "last-name")
        self.postcode = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.cancel_button = (By.ID, "cancel")

    def fill_account_info(self, info_firstname, info_lastname, info_code):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.firstname)).send_keys(info_firstname)
        wait.until(EC.element_to_be_clickable(self.lastname)).send_keys(info_lastname)
        wait.until(EC.element_to_be_clickable(self.postcode)).send_keys(info_code)
        #self.driver.find_element(*self.firstname).send_keys(info_firstname)
        #self.driver.find_element(*self.lastname).send_keys(info_lastname)
        #self.driver.find_element(*self.postcode).send_keys(info_code)

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    def click_finish_button(self):
        self.driver.find_element(*self.finish_button).click()

    def click_cancel_button(self):
        self.driver.find_element(*self.cancel_button).click()
