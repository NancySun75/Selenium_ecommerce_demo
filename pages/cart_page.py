from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

    def get_cart_items(self):
        items = self.driver.find_elements(*self.cart_items)
        return [item.text for item in items]

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def remove_item_button(self, product_name):
        remove_item_id = f"remove-{product_name}"
        self.driver.find_element(By.ID, remove_item_id).click()



