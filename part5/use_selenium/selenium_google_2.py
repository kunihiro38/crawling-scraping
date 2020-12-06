import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


options = Options()
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.co.jp/')

# タイトルにgoogleが含まれていることを確認する
assert 'Google' in driver.title

# 検索語を入力して送信する
input_element = driver.find_element_by_name('q')
input_element.send_keys('django')
input_element.send_keys(Keys.RETURN)
# タイトルに'Python'が含まれていることを確認する
assert 'django' in driver.title

# スクリーンショットを撮る
driver.save_screenshot('django_result.png')


