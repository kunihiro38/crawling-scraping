'''scraping'''
import csv
from typing import List

import requests
import lxml.html

def main():
    '''
    メイン処理
    '''
    url = 'https://gihyo.jp/dp'
    html = fetch(url)
    books = scrape(html, url)
    save('books.csv', books)

def fetch(url: str) -> str:
    '''
    引数URLで与えられたURLのwebページを取得する。
    webページのエンコーディングはContent-Typeヘッダーから取得する。
    戻り値:str型のHTML
    '''
    r = requests.get(url)
    return r.text # HTTPヘッダーから取得したエンコーディングでデコードした文字列を返す。


def scrape(html: str, base_url: str) -> List[dict]:
    '''
    引数htmlで与えられたHTMLから正規表現で書類の情報を抜き出す。
    引数base＿urlは絶対URLに変換する際の基準となるURLを指定する。
    戻り値：書籍(dict)のリスト
    '''

    books = []
    html = lxml.html.fromstring(html)
    html.make_links_absolute(base_url) # 全てのa要素のhref属性を絶対URLに変換する。
    # cssselect()メソッドで、セレクターに該当するa要素のリストを取得して、個々のa要素に対して処理を行う。
    # セレクターの意味：id="listBook"である要素の直接の子であるli要素の直接の子である itemprop = "url"という属性を持つa要素
    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        # a要素のhref属性から書類のURLを取得する。
        url = a.get('href')
        
        # 書籍のタイトルは itemprop="name" という属性を持つp要素から取得する。
        p = a.cssselect('p[itemprop="name"]')[0]
        title = p.text_content() # wbr要素などが含まれるのでtextではなくtext_content()を使う。

        books.append({'url': url, 'title': title})

    return books


def save(file_path: str, books: List[dict]):
    '''
    引数booksで与えられた書籍のリストをCSV形式のファイルに保存する。
    ファイルのパスは引数file_pathで与えられる。
    戻り値：なし
    '''

    with open(file_path, 'w', newline='') as f:
        # 第一引数にファイルオブジェクトを、第二引数にフィールド名のリストを指定する。
        writer = csv.DictWriter(f, ['url', 'title'])
        writer.writeheader() # 1行目のヘッダーを出力する、
        # writerows()で複数の行を一度に出力する。引数は辞書のリスト。
        writer.writerows(books)


if __name__ == '__main__':
    main()
