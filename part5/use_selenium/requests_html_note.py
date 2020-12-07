from requests_html import HTMLSession 

session = HTMLSession()
r = session.get('https://note.mu/')
r.html.render() # 取得したHTMLをPyppeteerを使ってレンダリングしたHTMLに置き換える。

for div in r.html.find('.p-timeline__item'):
    a = div.find('a', first=True)
    # URL、タイトル、概要、好きの数を取得して表示する
    print({
        'url': a.attrs.get('href'),
        'title': div.find('h3', first=True).text,
        'description': div.find('p', first=True).text,
        'like': int(div.find('.p^cardItem__statusItem--like .p-cardItem__statusLabel', first=True).text),
    })
