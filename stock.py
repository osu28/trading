import pandas as pd
from datetime import date
from IPython.display import display
from iexfinance.stocks import get_historical_data, get_historical_intraday
from plotnine import *

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

# historical_data = get_historical_data("MSFT", output_formate = 'pandas', token = api_key)
historical_intraday = get_historical_intraday("MSFT", output_formate = 'pandas', token = api_key)

display(historical_intraday)

# x = list(range(len(historical_intraday['label'])))
plot = (ggplot(data=historical_intraday, mapping=aes(x = 'historical_intraday.index', y= 'average'))
        + ggtitle('MSFT')
        + xlab('Time')
        + ylab('Market Average')
        + geom_line())
print(plot)