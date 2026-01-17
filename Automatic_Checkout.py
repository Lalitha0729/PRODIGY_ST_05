Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
... from selenium.webdriver.common.by import By
... from selenium.webdriver.common.action_chains import ActionChains
... import time
... import os
... 
... if not os.path.exists("screenshots"):
...     os.makedirs("screenshots")
... 
... driver = webdriver.Chrome()
... driver.maximize_window()
... 
... driver.get("http://www.automationpractice.pl/index.php")
... time.sleep(2)
... 
... driver.find_element(By.CLASS_NAME, "login").click()
... time.sleep(2)
... 
... driver.find_element(By.ID, "email").send_keys("testuser123@gmail.com")
... driver.find_element(By.ID, "passwd").send_keys("Test@123")
... driver.find_element(By.ID, "SubmitLogin").click()
... time.sleep(3)
... 
... driver.save_screenshot("screenshots/login.png")
... 
... product = driver.find_element(By.CSS_SELECTOR, ".product-container")
... ActionChains(driver).move_to_element(product).perform()
... time.sleep(1)
... 
... driver.find_element(By.CSS_SELECTOR, ".ajax_add_to_cart_button").click()
... time.sleep(3)
... 
... driver.save_screenshot("screenshots/product_added.png")
... 
... driver.find_element(By.XPATH, "//a[@title='Proceed to checkout']").click()
... time.sleep(3)
... 
... driver.find_element(By.XPATH, "//a[contains(@class,'standard-checkout')]").click()
... time.sleep(3)
... 
... driver.save_screenshot("screenshots/address.png")
... driver.find_element(By.NAME, "processAddress").click()
... time.sleep(2)
... 
... driver.find_element(By.ID, "cgv").click()  # Agree terms
driver.save_screenshot("screenshots/shipping.png")
driver.find_element(By.NAME, "processCarrier").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "bankwire").click()
time.sleep(2)
driver.save_screenshot("screenshots/payment.png")

driver.find_element(By.XPATH, "//button[contains(@class,'button-medium')]").click()
time.sleep(3)

success_text = driver.find_element(By.CSS_SELECTOR, ".cheque-indent strong").text

if "complete" in success_text.lower():
    print("✅ Order placed successfully")
else:
    print("❌ Order failed")

driver.save_screenshot("screenshots/order_success.png")

driver.quit()
