from selenium import webdriver
import pdb

driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Arun")

driver.find_element_by_css_selector("input[name='name']").send_keys("Arun")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_name("email").send_keys("arunagiriperumal@gmail.com")
driver.find_element_by_xpath("//input[@type='submit']").click()
#driver.minimize_window()