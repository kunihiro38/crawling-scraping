# 参考 http://docs.tweepy.org/en/latest/
# 参考 https://qiita.com/sugarcoder18/items/e66f6043fc17528f81ab

import sys
import tweepy
import time
import MeCab
import numpy
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS # 単語の頻出頻度の可視化

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

# \n改行除去 \t空白除去
j = " ".join([i.split("\t")[0] for i in text.split("\n")])
# print(j)
# 含めたくないワードを追加
add_STOPWORDS = ["この","たち","総理","まし","です","ます","から","いる","ない","する","ある","なる","れる","できる","これ","こと","さん","られる","やる","てる","ませ","その"] #表示させないキーワードを追加する
for word in add_STOPWORDS:
    STOPWORDS.add(word)

str(STOPWORDS)
st_text = text.encode("utf-8")

# Taggerというクラスのインスタンスを生成し、parseというメソッドを呼ぶことで解析結果が文字列として取得できる。

tagger = MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(j)


word_list = []
while node:
    word_type = node.feature.split(',')[0]
    word_surf = node.surface.split(',')[0]
    if word_type == '名詞' and word_surf not in add_STOPWORDS:
        word_list.append(node.surface)
    node = node.next
    
word_chain = ' '.join(word_list)
word_cloud = WordCloud(
    width=480,
    height=320,
    background_color = "white",
    max_words = 2000,
    font_path = "/Library/Fonts//ヒラギノ丸ゴ ProN W4.ttc" 
)
word_cloud.generate(word_chain)
word_cloud.to_file('sample.jpg')
file = open('sample.jpg')



# フォントパスはインストールしていない。最初からあるやつ。