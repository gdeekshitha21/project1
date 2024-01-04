river=wevdriver.chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

username_input=driver.find_element_by_id("username")
username_input=driver.find_element_by_id("password")
username_input.send_keys("your_username")
username_input.send_keys("ypur_password")
password_input.send_keys(Keys.ENTER)

Delete_existing_employee_button=driver.find_element_by_id("Delete_employee_button")
Delete_existing_employee_button_employee_button.click()

first_name_input=driver.find_element_by_id("first_name")
last_name_input=driver.find_element_by_id("lasr_name")
first_name_input.send_keys("joe")
last_name_input.send_keys("paul")
employee_id_input.send_keys("12345678")

save_button=driver.find_element_by_id("save_button")
save_button.click()
driver.quit()
