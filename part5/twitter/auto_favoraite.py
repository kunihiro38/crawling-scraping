# 参考 http://docs.tweepy.org/en/latest/
import os
import tweepy
import time

from dotenv import load_dotenv
load_dotenv()

# 取得した各種キーを格納-----------------------------------------------------
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# 取得したいキーワード
search_list = ['#駆け出しエンジニア', '#python']
search_list = ['#今日の積み上げ', '#駆け出しエンジニア']
# search_list = ['会社辞めたい', '駆け出しエンジニア', '転職']

# ツイート件数を入れた数だけいいねする
# ちなみにいいねは24時間で1000件が上限で、それを超えるとペナルティ(アカウント停止)を受ける
tweet_count = 50

for search in search_list:
    # サーチ結果
    search_result = api.search(q=search, count=tweet_count)
    for tweet in search_result:
        tweet_id = tweet.id
        try:
            api.create_favorite(id=tweet_id)
            print('いいね!!をしました')
            time.sleep(5) 
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
