import pandas as pd

df_exchange = pd.read_csv('exchange.csv', header=1, names=['date', 'USD', 'rate'], index_col=0, parse_dates=True)

print(df_exchange)