from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as Wait

# Each browser has an executable file which can be exposed to selenium.
# Selenium do not have direct command to open browser from our desktop
# So in test we have to invoke the browser executable file so it kicks in.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# path = "/Users/apple/Documents/GITHUB-UDEMY-TUTORIAL/Python-Selenium/Selenium-intro/chromedriver"
# driver = webdriver.Chrome(executable_path="./chromedriver")
# driver is an object created with - webdriver, a package and chrome is one class in the package.


print(driver.title)
print(driver.current_url)


