
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\Selenium-Python\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("http://www.demo.guru99.com/v4/")

driver.find_element(By.NAME,"uid").send_keys("mngr481080")
driver.find_element(By.NAME,"password").send_keys("majevYp")
driver.find_element(By.NAME,"btnLogin").click()
print("Login success")
driver.close()