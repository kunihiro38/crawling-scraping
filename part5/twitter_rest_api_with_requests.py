'''
参考 https://tech-lab.sios.jp/archives/21400
'''
import tweepy

# 取得した各種キーを格納-----------------------------------------------------
consumer_key = "C9owTyqBxpMpHpdii5mxKilre"
consumer_secret = "yFI4hNklHSxvcvCvNhnqBflXiktgm0TYcDYdoL1FsK3xtsBQft"
access_token = "953993444099219456-JAZgNgQZYHzqO1D7PEwGgGckMGwD6Uh"
access_token_secret = "lTk2kM0l47Ggv9AgtUOD7Oz7yGh5FgJJdxsncuXvWkCR4"

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status("テスト投稿!!")
