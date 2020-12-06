
import logging
import chromedriver_binary
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def main():
    """メインの処理
    """
    # web立ち上げ
    options = Options()
    # ヘッドレスモードを有効にするには、次の行のコメントアウトを解除する
    # options.headless = True
    driver = webdriver.Chrome(options=options)
    # driver.get('https://www.google.co.jp/')
    navigate(driver) # noteのトップページに遷移する
    contents = scrape_contents(driver) # コンテンツのリストを取得する
    logging.info(f'Found {len(contents)} contents.') # 取得したコンテンツの数を表示する
    
    # コンテンツの情報を表示する。
    for content in contents:
        print(content)


def navigate(driver):
    """目的のページに遷移する。
    """
    logging.info('Navigating...')
    driver.get('https://note.mu/') # noteのトップページを開く
    assert 'note' in driver.title # タイトルにnoteが含まれていることを確認する。

def scrape_contents(driver) -> List[dict]:
    """文章コンテンツのURL、タイトル、概要、好きの数を含むdictのリストを取得する
    """
    contents = [] # 取得したコンテンツを格納するリスト

    # コンテンツを表すdiv要素について反復する。
    for div in driver.find_elements_by_css_selector('.o-timeline__item'):
        a = div.find_elements_by_css_selector('a')
        print(a)
        try:
            description = div.find_elements_by_css_selector('p').text
        except NoSuchElementException:
            description = '' # 画像コンテンツなどp要素がない場合はから文字にする。
        
        # URL、タイトル、概要、好きの数を取得してdictとしてリストに追加する。
        contents.append({
            'url': a.get_attribute('href'),
            'title': div.find_elements_by_css_selector('h3').text,
            'description': description,
            'like': int(div.find_elements_by_by_css_selector('.o-noteStatus__item--like .o-noteStatus__label').text),
        })

        return contents






if __name__=='__main__':
    main()

