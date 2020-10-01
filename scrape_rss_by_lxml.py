'''scrape_rss_by_lxml'''
# import lxml.etree # lxml.etreeモジュールをインポートする
from xml.etree import ElementTree
# parse()関数でファイルを読み込んでElementTreeオブジェクトを得る。
tree = ElementTree.parse('rss2.xml')
# getroot()メソッドでXMLのルート要素(この例ではres要素)に対応するElementオブジェクトを得る。
root = tree.getroot()

# xpath()メソッドでxPathにマッチングする要素のリストを取得する。
# channel/item はchannel要素の子要素であるitem要素を表す。
for item in root.xpath('channel/item'):
    title = item.xpath('title')[0].text # item要素内にあるtitle要素の文字列を取得する。
    url = item.xpath('link')[0].text # item要素内にあるlink要素の文字列を取得する。
    print(url, title)
