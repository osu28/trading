import pandas as pd
from datetime import date
import re
from IPython.display import display
from iexfinance.stocks import get_historical_data, get_historical_intraday
from plotnine import *
import matplotlib.pyplot as plt
import numpy
import time

import json
import pprint
from sseclient import SSEClient

#api key for iex finance
api_key = "pk_57654da99c1e468d8b3a5143b498cf20"


# dataframe display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

# current date
today = date.today()

# def with_urllib3(url, headers):
#     """Get a streaming response for the given event feed using urllib3."""
#     import urllib3
#     http = urllib3.PoolManager()
#     return http.request('GET', url, preload_content=False, headers=headers)
#
# def with_requests(url, headers):
#     """Get a streaming response for the given event feed using requests."""
#     import requests
#     return requests.get(url, stream=True, headers=headers)

messages = SSEClient('https://cloud-sse.iexapis.com/stable/stocksUSNoUTP?token=pk_57654da99c1e468d8b3a5143b498cf20&symbols=spy')


hl, = plt.plot([], []) # dynamically updating line plot
time = 0

def update_line(hl, new_price, seconds):
    hl.set_xdata(numpy.append(hl.get_xdata(), seconds))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_price))
    print("Updated")
    plt.draw()

for msg in messages:
    time += 1
    data = msg.data
    price = re.search('(?<="iexBidPrice":)(.*?)(?=,)', data).group()
    print(price)
    # update_line(hl, price, time)




# plot = (ggplot(data=historical_intraday, mapping=aes(x = 'historical_intraday.index', y= 'average'))
#         + ggtitle('MSFT')
#         + xlab('Time')
#         + ylab('Market Average')
#         + geom_line())
# print(plot)