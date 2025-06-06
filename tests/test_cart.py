import unittest
from utils.driver_setup import create_driver
from config import settings
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver()
        self.driver.get(settings.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_to_cart_by_name(settings.ITEM_NAME_BACKPACK)

    def test_get_cart_items(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        self.assertIn("cart", self.driver.current_url)
        cart_items = cart_page.get_cart_items()
        print("items in the cart:", cart_items)

    def test_click_checkout(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        self.assertIn("checkout", self.driver.current_url)

    def test_cart_remove_item(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        self.assertIn("cart", self.driver.current_url)
        cart_page.remove_item_button(settings.ITEM_NAME_BACKPACK)
        cart_items = cart_page.get_cart_items()
        self.assertTrue(all(settings.ITEM_NAME_BACKPACK not in item for item in cart_items))


    def tearDown(self):
        self.driver.quit()