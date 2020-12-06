import time
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get('https://www.google.co.jp/')
search_box= driver.find_element_by_name("q")
search_box.send_keys("いつやるか今でしょう")
search_box.submit()
time.sleep(5)
driver.quit()