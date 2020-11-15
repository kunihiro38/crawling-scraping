import tweepy
import time

CONSUMER_KEY        = '自分のconsumer key'
CONSUMER_SECRET_KEY = '自分のconsumer secret key'
ACCESS_TOKEN        = '自分のaccess token'
ACCESS_TOKEN_SECRET = '自分のaccess token key'
SCREEN_NAME         = '自分のアカウントID'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

word = ["抽選"]
set_count = 70

results = api.search(q=word, lang="ja",count = set_count, result_type = "popular",since = "2020-6-8")

for result in results:
    username = result.user._json['screen_name']
    tweet_id = result.id
    user = result.user.screen_name
    api.create_friendship(username)


    try:
        api.create_favorite(tweet_id)
        api.retweet(tweet_id)
        print("アカウント名:" +str(user) +"に応募")
        #time.sleep(1)
    except:
        print("既に応募済みです。")

# 参考 https://note.com/katomaru0510/n/n8797618a68ce