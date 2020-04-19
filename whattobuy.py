import pandas as pd
import datetime 
from datetime import date, timedelta
import pandas_datareader.data as web
from operator import itemgetter 
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = data[0]
tickers = table['Symbol'].tolist()
print('welcome to Elam\'s s&p 500 dip calculator!')
tume = input("from how many days ago?")
timeframe = date.today() - timedelta(days=int(tume))
end = date.today()
start = timeframe
finaldiff = []
for i in tickers: 
    print('Analyzing ' + i + "...")
    prev = 0
    if "." in i:
        continue
    try:
        df = web.DataReader(name=i, data_source='yahoo', start=start, end=end)
    except KeyError:
        pass
    for j in df.iterrows(): 
        if prev == 0:
            prev = [i,j[1][3]]
        else:
            if prev[1] > j[1][3]:
                prev = [i,j[1][3]]
    prev[1] = round((1 - prev[1] / df["Close"][-1]),2) 
    finaldiff.append(prev)
finaldiff = sorted(finaldiff, key = itemgetter(1)) 
bottomx = int(input('Complete the sentance: I would like to see the top (x) s&p 500 companies cloest to their ' + tume + '-day low'))
for i in range(bottomx):
    if finaldiff[i][1] == 0:
        print(finaldiff[i][0] + " is at its " + tume + '-day low!')
    else:
        print(finaldiff[i][0] + " is " + str(finaldiff[i][1]) + "% above its " + tume + '-day low')