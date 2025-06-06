import unittest
from utils.driver_setup import create_driver
from config import settings
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver()

    def test_successful_login(self):
        self.driver.get(settings.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.login(settings.USERNAME, settings.PASSWORD)
        self.assertIn("inventory", self.driver.current_url)

    def test_failed_login(self):
        self.driver.get(settings.BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "wrong_password")
        error_text = login_page.get_error_message()
        self.assertIn("Username and password do not match", error_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

