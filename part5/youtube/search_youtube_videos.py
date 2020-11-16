import os

# from apiclient.discovery import build # これが動かなければ下のコードに
from googleapiclient.discovery import build

from dotenv import load_dotenv
load_dotenv()

YOUTUBE_API_KEY = os.environ['YOUTBUE_API_KEY']


# YouTubeのAPIクライアントを組み立てる。
# build()関数の第一引数にはAPI名
# 第二引数にはAPIのバージョンを指定し、キーワード引数developerKyeでAPIキーを指定する。

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# キーワード引数で引数を指定し、search.listメソッドを呼び出す
# list()メソッドでgoogleapiclient.http.httprequestオブジェクトが得られ
# execute()メソッドを実行すると実際にHTTPリクエストが送られて、APIのレスポンスが得られる。

search_response = youtube.search().list(
    part='snippet',
    # 検索したい文字列を指定
    q='テキサスホールデム',
    # 視聴回数が多い順に取得
    order='viewCount',
    type='video',
).execute()

# search_responseはAPIのレスポンスのJSONをパースしたdict
for item in search_response['items']:
    print(item['snippet']['title']) #　動画のタイトルを表示する。

