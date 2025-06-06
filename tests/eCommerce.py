from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.driver_setup import get_driver
from utils.screenshot_help import take_screenshot
from datetime import datetime

# 登录页面
def login(driver, username_text, password_text):
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys(username_text)
    driver.find_element(By.ID, "password").send_keys(password_text)
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html")) # 登录后要确保页面跳转成功
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    print("登录成功，进入商品页面")

# 获取商品页面内容
def product_page(driver):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    print(f"商品数量：{len(products)}")
    for product in products:
        print("商品名称：", product.text)
    assert len(products) == 6

# 添加购物车
def add_to_cart(driver, product_id, remove_id):
    wait = WebDriverWait(driver, 30)
    product = wait.until(EC.visibility_of_element_located((By.ID, product_id)))
    product.click()
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.ID, remove_id)))
    print(f"✅ 商品 {product_id} 已成功加入购物车")

# 查看购物车商品数量
def get_cart_count(driver):
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    count = int(cart_badge.text)
    print(f"购物车商品数量：{count}")
    return count

# 查看购物车内商品
def check_cart_items(driver):
    cart = driver.find_element(By.ID, "shopping_cart_container")
    cart.click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    item_names = [item.text for item in cart_items]
    print("🛒 购物车中商品：")
    for name in item_names:
        print(name)
    return item_names

# 不结账选择继续购物
def continue_shopping(driver):
    continue_shopping = driver.find_element(By.ID, "continue-shopping")
    continue_shopping.click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    print("返回商品页面")

# 购物结束，准备结账
def checkout(driver, first_name_text, last_name_text, postcode_text):
    wait = WebDriverWait(driver, 5)
    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()
    firstname = driver.find_element(By.ID, "first-name")
    lastname = driver.find_element(By.ID, "last-name")
    postcode = driver.find_element(By.ID, "postal-code")
    firstname.send_keys(first_name_text)
    lastname.send_keys(last_name_text)
    postcode.send_keys(postcode_text)
    driver.find_element(By.ID, "continue").click()
    wait.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
    driver.find_element(By.ID, "finish").click()
    wait.until(EC.url_contains("checkout-complete"))
    assert driver.find_element(By.CLASS_NAME, "complete-header").text == "Thank you for your order!"
    print("购物成功")

#启动浏览器
driver = get_driver()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
current_time = datetime.now().strftime("%Y%m%d")

login(driver, "standard_user", "secret_sauce")
take_screenshot(driver, "saucedemo_logged_in.png")
product_page(driver)
add_to_cart(driver, "add-to-cart-sauce-labs-backpack", "remove-sauce-labs-backpack")
get_cart_count(driver)
check_cart_items(driver)
continue_shopping(driver)
add_to_cart(driver, "add-to-cart-test.allthethings()-t-shirt-(red)", "remove-test.allthethings()-t-shirt-(red)")
get_cart_count(driver)
check_cart_items(driver)
checkout(driver, "standard_user", "secret_sauce", current_time)
driver.quit()

"""
# 各个item 关于“add to cart” button 的定位
backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
bikeLight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
boltT_shirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
fleeceJacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
redT_shirt = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
"""



