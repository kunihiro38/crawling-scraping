# 参考 https://www.mof.go.jp/jgbs/reference/interest_rate/index.htm
import pandas as pd
from datetime import datetime

def parse_japanese_date(s):
    base_years = {'S': 1925, 'H': 1988, 'R': 2018} # 昭和以降の元号の0年に相当する年を定義しておく
    era = s[0] # 元号を表すアルファベット1文字を
    year, month, day = s[1:].split('.') # 2文字目以降を.(ピリオド)で分割して年月日に分ける。
    year = base_years[era] + int(year) # 元号の0年に相当する年と数値に変換した年を足して西暦の年を得る。
    return datetime(year, int(month), int(day)) # datetimeオブジェクトを作成する

df_jgbcom = pd.read_csv(
    'jgbcm_all.csv', 
    header=1,
    index_col=0,
    parse_dates=True,
    date_parser=parse_japanese_date,
    na_values=['-']
)

print(df_jgbcom)