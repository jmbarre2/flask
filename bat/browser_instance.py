from selenium import webdriver

driver_path = 'C:\Python3\chromedriver_win32\chromedriver.exe'
url = 'localhost:5000'

browser = webdriver.Chrome(driver_path)
browser.get(url)
