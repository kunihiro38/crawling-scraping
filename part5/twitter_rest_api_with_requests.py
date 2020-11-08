'''
参考 https://tech-lab.sios.jp/archives/21400
'''
import tweepy

# 取得した各種キーを格納-----------------------------------------------------
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

for status in public_tweets:
    print('@' + status.user.screen_name, status.text)

# api.update_status("テスト投稿!!")
