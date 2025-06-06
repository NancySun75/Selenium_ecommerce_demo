from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_items = (By.CLASS_NAME, "inventory_item_name")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def show_all_items(self):
        items = self.driver.find_elements(*self.product_items)
        return [item.text for item in items]

    def add_to_cart_by_name(self, product_name):
        add_item_id = f"add-to-cart-{product_name}"
        remove_item_id = f"remove-{product_name}"
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.ID, add_item_id))).click()
        wait.until(EC.visibility_of_element_located((By.ID, remove_item_id)))

    def add_multiple_items_to_cart(self, product_names):
        for name in product_names:
            self.add_to_cart_by_name(name)

    def get_cart_count(self):
        # if the cart is null, the cart badge won't exist and an exception need to be considered
        try:
            count = int(self.driver.find_element(*self.cart_badge).text)
        except:
            count = 0
        return count








