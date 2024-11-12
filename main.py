import time
import warnings
import schedule
import requests
import pandas as pd
from constants import EXCHANGE
from fetch_data_from_exchange import FetchData
from tech_indicators import TechIndicators
from place_order import PlaceOrders
pd.set_option('display.max_rows', None)

warnings.filterwarnings('ignore')


class MainBot:
    def __init__(self) -> None:
        pass

    def run_bot(self):
        fetch_balance = EXCHANGE.fetch_balance()
        bal_stable = fetch_balance['total']['USDT']
        if(bal_stable > 1) or (alt =='BTC' and bal_alt > 0.001) or (alt =='ETH' and bal_alt > 0.01) or (bal_alt > 0.1):
                alt, _, _, bal_stable, bal_alt, _, high_data, low_data = FetchData().fetch_data_from_exchange()
        rsi, upper, _, lower = TechIndicators().rsi_BBand()
        if((rsi < 30) and (low_data < lower)):
            buy_order = PlaceOrders().buy_order()
            print(alt +' buy order is '+str(buy_order))        
        if(rsi > 70 and high_data > upper and bal_alt > 0.0001):
            _, sell_order = PlaceOrders().sell_order()
            print(alt+' sell order is '+str(sell_order))
   

try:
    mainfunc = MainBot()
    schedule.every(15).seconds.do(mainfunc.run_bot())
    while True:
        schedule.run_pending()
        time.sleep(1)
except requests.HTTPError as exception:
    pass