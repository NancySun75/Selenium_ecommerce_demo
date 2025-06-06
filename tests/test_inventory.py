import unittest
from utils.driver_setup import create_driver
from config import settings
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver()
        self.driver.get(settings.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)

    def test_show_all_items(self):
        inventory_page = InventoryPage(self.driver)
        item_names = inventory_page.show_all_items()
        self.assertGreater(len(item_names), 0)
        print("Available items:", item_names)

    def test_add_item_cart(self):
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_to_cart_by_name(settings.ITEM_NAME_BACKPACK)
        count = inventory_page.get_cart_count()
        self.assertEqual(count, 1)

    def test_add_multiple_items_to_cart(self):
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_multiple_items_to_cart([
            settings.ITEM_NAME_BACKPACK,
            settings.ITEM_NAME_BIKELIGHT,
            settings.ITEM_NAME_BOLTT_SHIRT
        ])
        count = inventory_page.get_cart_count()
        self.assertEqual(count, 3)

    def tearDown(self):
        self.driver.quit()