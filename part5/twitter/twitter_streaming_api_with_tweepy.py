import os

import tweepy

# 取得した各種キーを格納-----------------------------------------------------
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def main():
    '''
    メインとなる処理
    '''
    # OAuthHandlerオブジェクトを作成し、認証情報を設定する
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # OAuthHandlerとStreamListenerを指定してStreamオブジェクトを取得する。
    stream = tweepy.Stream(auth, MyStreamListener())
    # 公開されているツイートをサンプリングしたストリームを受診する。
    #　キーワード引数languagesで、日本語のツイートのみに絞り込む。
    stream.sample(languages=['ja'])


class MyStreamListener(tweepy.StreamListener):
    '''
    Streaming APIで取得したツイートを処理するためのクラス。
    '''
    def on_status(self, status: tweepy.Status):
        '''
        ツイートを受診したときに呼び出されるメソッド。引数はツイートを表すStatusオブジェクト。
        '''
        print('@' +  status.author.screen_name, status.text)

if __name__=='__main__':
    main()




