import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt


start = dt.datetime(2019, 1, 1)

end = dt.datetime.now()

data = web.DataReader('TSLA', 'yahoo', start, end)

colors = mpf.make_marketcolors(up='#00ff00', down='#ff0000', wick='inherit', edge='inherit', volume='in') 
style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)
mpf.plot(data, type="candle", style=style)