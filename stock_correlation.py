import pandas as pd
from iexfinance.stocks import get_historical_data, get_historical_intraday
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

api_key = "pk_57654da99c1e468d8b3a5143b498cf20"

pd.set_option('display.max_columns', None)
# historical prices dataframes (index = date, columns [close, high, low, open, symbol, volume, changePercent]
spy_historical = get_historical_data("SPY", output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]
ivv_historical = get_historical_data("SPY", output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]
schg_historical = get_historical_data("SPY", output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]
spx_historical = get_historical_data("SPY", output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]

print(spy_historical["close"])
print(ivv_historical["close"])

model = LinearRegression().fit(spy_historical["close"].values.reshape(-1, 1), ivv_historical["close"].values.reshape(-1, 1))
r2 = model.score(spy_historical["close"].values.reshape(-1, 1), ivv_historical["close"].values.reshape(-1, 1))
print(r2)

plt.plot(spy_historical["close"])
plt.plot(ivv_historical["close"])
# plt.show()
