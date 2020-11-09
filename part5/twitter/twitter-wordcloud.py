# 参考 http://docs.tweepy.org/en/latest/

import tweepy
import time
import MeCab
import numpy
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS # 単語の頻出頻度の可視化


# 絵文字を除去する
def remove_emoji(src_str):
    return ''.join(c for c in src_str if ctnot in emoji.UNiCODE_EMOJI)


# 取得した各種キーを格納-----------------------------------------------------
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

Account = "Hiroyan_python"
tweets = api.user_timeline(Account, count=200, page=1)
num = 1
text = ''
# for tweet in tweets:
#     print('twid : ', tweet.id)               # tweetのID
#     print('user : ', tweet.user.screen_name)  # ユーザー名
#     print('date : ', tweet.created_at)      # 呟いた日時
#     print(tweet.text)                  # ツイート内容
#     print('favo : ', tweet.favorite_count)  # ツイートのいいね数
#     print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
#     print('ツイート数 : ', num) # ツイート数
#     print('='*80) # =を80個表示
#     num += 1 # ツイート数を計算
#     list += tweet.text

for tweet in tweets:
    text += tweet.text

# 改行除去
j = " ".join([i.split("\t")[0] for i in text.split("\n")])
print(j)

# 含めたくないワードを追加
add_STOPWORDS = ["この","たち","総理","まし","です","ます","から","いる","ない","する","ある","なる","れる","できる","これ","こと","さん","られる","やる","てる","ませ","その"] #表示させないキーワードを追加する
for word in add_STOPWORDS:
    STOPWORDS.add(word)


str(STOPWORDS)
st_text = text.encode("utf-8")
tagger = MeCab.Tagger("-Ochasen")
message = tagger.parse(text)
print(j)

# word
# wordcloud = WordCloud(
#     width=480,
#     height=320,
#     background_color = "white",
#     max_words = 2000,
#     font_path = "./hirakakupro-w4.otf" 
# )

# wordcloud.generate(j)
# wordcloud.to_file('sample.jpg')
# file = open('sample.jpg')


