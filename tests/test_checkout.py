import unittest
from utils.driver_setup import create_driver
from config import settings
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver()
        self.driver.get(settings.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_to_cart_by_name(settings.ITEM_NAME_BACKPACK)
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        cart_page.click_checkout()

    def test_checkout_successfully(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_account_info(settings.INFO_FIRSTNAME, settings.INFO_LASTNAME, settings.INFO_POSTCODE)
        checkout_page.click_continue_button()
        self.assertIn("step-two", self.driver.current_url)
        checkout_page.click_finish_button()
        self.assertEqual(self.driver.find_element(By.CLASS_NAME, "complete-header").text, "Thank you for your order!")
        print("购物成功")

 #   def test_checkout_without_info(self):

    def test_cancel_checkout(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_account_info(settings.INFO_FIRSTNAME, settings.INFO_LASTNAME, settings.INFO_POSTCODE)
        checkout_page.click_cancel_button()
        self.assertIn("cart", self.driver.current_url)