from urllib.parse import urljoin
from bs4 import BeautifulSoup # bs4モジュールからBeautifulSoupクラスをインポートする

# HTMLファイルを読み込んでBeautifulSoupオブジェクトを得る
with open('dp.html') as f:
    soup = BeautifulSoup(f, 'html.parser') # HTMLパースとは、HTML文法規則にのっとった文字列を、その文法に基づいて字句解析し、意味や構造を解釈することをいい、HTMLパースを行うプログラムのことをHTMLパーサといいます。

    # select()メソッドで、セレクターに該当するa要素のリストを取得して個々のa要素に対して処理を行う
    for a in soup.select('#listBook > li > a[itemprop="url"]'):
        # a要素のhref属性から書籍のURLを取得する。
        url = urljoin('http://gihyo.jp/dp', a.get('href'))

        # 書籍のタイトルは itemprop="name"という属性を持つp要素から取得する。
        p = a.select('p[itemprop="name"]')[0]
        title = p.text # wbr要素などが含まれるのでstringではなくtextを使う
        print(url, title)