import pandas as pd
from iexfinance.stocks import get_historical_data, get_historical_intraday
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

api_key = "pk_57654da99c1e468d8b3a5143b498cf20"

pd.set_option('display.max_columns', None)
# historical prices dataframes (index = date, columns [close, high, low, open, symbol, volume, changePercent]
# spy_historical = get_historical_data("SPY", output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]
# ivv_historical = get_historical_data("IVV", output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]
# schg_historical = get_historical_data("SCHG", output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]
# spx_historical = get_historical_data("AAPL", output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]

# print(spy_historical)
# print(ivv_historical)

symbols = ["SPY", "IVV", "SCHG", "AAPL"]
pool = []
for symbol in symbols:
    data = get_historical_data(symbol, output_format='pandas', token=api_key)[["symbol", "close", "changePercent", "volume"]]
    pool.append(data)



def correlation_score(history1, history2):
    model = LinearRegression().fit(history1["close"].values.reshape(-1, 1), history2["close"].values.reshape(-1, 1))
    r2 = model.score(history1["close"].values.reshape(-1, 1), history2["close"].values.reshape(-1, 1))
    return (history1["symbol"][0], history2["symbol"][0], r2)

for k in range(len(pool) - 1):
    for j in range(k + 1, len(pool)):
        correlation = correlation_score(pool[k], pool[j])
        print(correlation)

plt.plot(pool[0]["close"])
# plt.plot(pool[1]["close"])
plt.show()
