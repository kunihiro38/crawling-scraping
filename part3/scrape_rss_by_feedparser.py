'''feedparser'''
import feedparser

# はてなブックマークの人気エントリー(テクノロジー)のRSSを読み込む
d = feedparser.parse('http://b.hatena.ne.jp/hotentry/it.rss')

# 全ての要素について処理を繰り返す。
for entry in d.entries:
    print(entry.link, entry.title) # URLとタイトルを出力する