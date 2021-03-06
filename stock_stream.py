import pandas as pd
from datetime import date
import re
from IPython.display import display
from iexfinance.stocks import get_historical_data, get_historical_intraday
from plotnine import *
import matplotlib.pyplot as plt
import numpy
import time
import math

import json
import pprint
from sseclient import SSEClient

# api key for iex finance
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

def sigmoid(x):
    return 1 / (1 + math.exp(-x))


spy_messages = SSEClient(
    'https://cloud-sse.iexapis.com/stable/stocksUSNoUTP?token=pk_57654da99c1e468d8b3a5143b498cf20&symbols=spy')
ivv_messages = SSEClient(
    'https://cloud-sse.iexapis.com/stable/stocksUSNoUTP?token=pk_57654da99c1e468d8b3a5143b498cf20&symbols=ivv')

# hl, = plt.plot([], []) # dynamically updating line plot
time = 0
#
# def update_line(hl, new_price, seconds):
#     hl.set_xdata(numpy.append(hl.get_xdata(), seconds))
#     hl.set_ydata(numpy.append(hl.get_ydata(), new_price))
#     print("Updated")
#     plt.draw()

temp_value = 0


def get_metrics(msg):
    data = msg.data
    price = re.search('(?<="iexBidPrice":)(.*?)(?=,)', data).group()
    annual_high = re.search('(?<="week52High":)(.*?)(?=,)', data).group()
    annual_low = re.search('(?<="week52Low":)(.*?)(?=,)', data).group()
    annual_avg = (float(annual_high) + float(annual_low)) / 2
    # normalized = float(price)/annual_avg
    return price


def volatility_management(price, annual_avg):
    if abs(float(price) - float(annual_avg)) > 50:
        return annual_avg
    return price


def arbitrage_opportunity(security1, security2):
    difference_ratio = (security2 - security1) / (security2 + 1)
    if security1 >= security2:
        difference_ratio = (security1 - security2) / (security1 + 1)
    # print(difference_ratio)
    if 0.004 <= difference_ratio <= 0.1:
        # print("ARBITRAGE!!!")
        return True
    return False


for spy_msg, ivv_msg in zip(spy_messages, ivv_messages):
    time += 1
    try:
        spy = get_metrics(spy_msg)
        ivv = get_metrics(ivv_msg)
        # print("SPY: " + spy)
        # print("IVV: " + ivv)
        if arbitrage_opportunity(float(spy), float(ivv)):  # identifies if there is an arbitrage opportunity
            print("SPY: " + spy)
            print("IVV: " + ivv)

    except Exception as e:
        print("Exception: " + str(e))

    # update_line(hl, price, time)

# for spy_msg in spy_messages:
#     time += 1
#     spy_data = spy_msg.data
#     spy_price = re.search('(?<="iexBidPrice":)(.*?)(?=,)', spy_data).group()
#     print("SPY: " + spy_price)


# plot = (ggplot(data=historical_intraday, mapping=aes(x = 'historical_intraday.index', y= 'average'))
#         + ggtitle('MSFT')
#         + xlab('Time')
#         + ylab('Market Average')
#         + geom_line())
# print(plot)
