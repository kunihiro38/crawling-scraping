'''
test
'''
import os

import tweepy 

# from requests_oauthlib import OAuth1Session


# 環境変数から認証情報を取得する。
TWITTER_API_KEY = os.environ.get('aStomqqVIkeZ1QCgdoQGzTR5f')
TWITTER_API_SECRET_KEY = os.environ.get('YNHOGN6ELKat7QkSbCEoLoCGexYl09XKryemj1GaNCHZKBPV2o')
TWITTER_ACCESS_TOKEN = os.environ.get('953993444099219456-KCOiveyV1z8B8QBl9Hs7uJ45AuS3SA3')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('XPzgRlXPA9Bl3I7fsltWHTAm1YN6XEO4KRkuK4fPm6ChZ')


# 認証情報を使ってOAuth1Sessionオブジェクトを得る。
# twitter = OAuth1Session(TWITTER_API_KEY,
#                         client_secret=TWITTER_API_SECRET_KEY,
#                         resource_owner_key=TWITTER_ACCESS_TOKEN,
#                         resource_owner_secret=TWITTER_ACCESS_TOKEN_SECRET)


auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

for status in public_tweets:
    print('@' + status.user.screen_name, status.text)