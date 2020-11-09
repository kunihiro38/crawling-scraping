# 参考 http://docs.tweepy.org/en/latest/

import tweepy
import time

# 絵文字を除去する
def remove_emoji(src_str):
    return ''.join(c for c in src_str if ctnot in emoji.UNiCODE_EMOJI)


# 取得した各種キーを格納-----------------------------------------------------
CONSUMER_KEY = "ADszgSxou1TsAD076fuslsLEG"
CONSUMER_SECRET = "RN3yhLzJHOnqPUfURXEFCQxU9D8teaWLMVMwZqL7JjD6bxTii6"
ACCESS_TOKEN = "953993444099219456-WaIffLmlu3LfHxVMiDQhG7h8XCXIOHv"
ACCESS_TOKEN_SECRET = "FksrWC9znitAMnOHrKGy0hZ9Rcw2xAvAhod3SG1iPtvXs"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# 取得したいキーワード
search_list = ['#駆け出しエンジニア', '#python']
search_list = ['#今日の積み上げ', '#駆け出しエンジニア']

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
