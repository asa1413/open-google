from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\arosenzweig\PycharmProjects\python\chromedriver.exe")
#driver.get("https://www.ynet.co.il")
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("dog")
tip_xpath = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]')
tip_xpath.click()
print(good)
