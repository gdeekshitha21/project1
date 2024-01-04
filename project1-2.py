driver=webdriver.chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
username_input=driver.find_element_by_id("username")
password_input=driver.find_element_by_id("password")

username_input.send_keys("Admin")
password_input.send_keys("admin123")
password_input.send_keys(Keys.ENTER)
click.login()

driver.find_elements_by_id("error-message").text
test_login_with_ib=nvalidvalid_credentials()