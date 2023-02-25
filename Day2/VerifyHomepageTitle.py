
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("Drivers/chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("http://www.demo.guru99.com/v4/")

driver.find_element(By.NAME,"uid").send_keys("mngr481080")
driver.find_element(By.NAME,"password").send_keys("majevYp")
driver.find_element(By.NAME,"btnLogin").click()

act_title=driver.title
exp_title="Guru99 Bank Manager HomePage"
if act_title==exp_title:
    print("Login success")
else:
    print("Login Failed")
    print("Check your creditionals")
driver.close()