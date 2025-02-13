    # Python program Continued
# Webdriver For Firefox
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://mbasic.facebook.com")
html = driver.page_source # Getting Source of Current URL / Web-Page Loaded
print(html)
# End
