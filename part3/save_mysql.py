import MySQLdb

conn = MySQLdb.connect(db='scraping', user='scraper', passwd='password', charset='utf8mb4')

c = conn.cursor() # カーソルを取得する。

# execute()メソッドでSQL文を実行する。
# このスクリプトを何回実行しても同じ結果になる様にするため、citiesテーブルが存在する場合は削除する。
c.execute('DROP TABLE IF EXISTS cities')
# citiesテーブルを作成する。
c.execute('''
    CREATE TABLE `cities` (
        `rank` integer,
        `city` text,
        `population` integer
    )
''')

# execute()メソッドの第二引数にはSQL文のパラメーターのリストを指定できる。
# パラメーターで置き換える場所(プレースホルダー)は%sで指定する。
c.execute('INSERT INTO cities VALUES (%s, %s, %s)', (1, '上海', 2415000))

# パラメーターが辞書の場合、プレースホルダーは%(名前)sで指定する。
c.execute('INSERT INTO `cities` VALUES (%(rank)s, %(city)s, %(population)s)',
            {'rank': 2, 'city': 'カラチ',  'population': 23500000})

# executemany()メソッドでは、複数のパラメーターをリストで指定できる。
# パラメーターの数(ここでは3つ)のSQLを順に実行できる。
c.executemany('INSERT INTO `cities` VALUES (%(rank)s, %(city)s, %(population)s)', [
        {'rank':3, 'city': '北京', 'population': 21516000},
        {'rank':4, 'city': '天津', 'population': 14722100},
        {'rank':5, 'city': 'イスタンブル', 'population': 14160467},
])

conn.commit() # 変更をコミット(保存)する。

c.execute('SELECT * FROM cities') # 保存したデータを取得するSELECT文を実行する。
for row in c.fetchall(): # クエリの結果はfetchall()メソッドで取得できる。
    print(row) # 保存したデータを表示する

conn.close() # コネクションを閉じる。
