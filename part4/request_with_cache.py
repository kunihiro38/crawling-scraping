import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache

session = requests.Session()
# sessionをラップしたcached_sessionを作る
# キャッシュはファイルとしてwebcacheディレクトリ内に保存する。
cached_session = CacheControl(session, cache=FileCache('.webcache'))

response = cached_session.get('https://docs.python.org/3/') # 通常のsessionと同様に使用する

# response.from_cache属性でキャッシュから取得されたレスポンスかどうかを取得できる。
print(f'from_cache: {response.from_cache}')
print(f'status_code: {response.status_code}')
print(response.text)