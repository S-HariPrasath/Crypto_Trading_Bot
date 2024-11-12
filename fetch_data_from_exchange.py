import pandas as pd
import pytz
from constants import BAL_ALT, EXCHANGE
from datetime import datetime

class FetchData:
    def __init__(self) -> None:
        pass

    def fetch_data_from_exchange(self):
        fetch_balance = EXCHANGE.fetch_balance()
        bal_stable = fetch_balance['total']['USDT']
        for alt in BAL_ALT :
            print('USDT bal = '+str(bal_stable))
            bal_alt = fetch_balance['total'][alt]
            print(alt+" bal = "+str(bal_alt))
            bids = EXCHANGE.fetch_order_book(alt+'/USDT')
            bids = bids['bids'][0][0]
            print(alt+' bid = '+str(bids))
            asks = EXCHANGE.fetch_order_book(alt+'/USDT')
            asks = asks['asks'][0][0]
            print(alt+' ask = '+str(asks))
            print(f"Fetching new bars for {datetime.now(pytz.timezone('Asia/Kolkata')).isoformat()}")
            bars = EXCHANGE.fetch_ohlcv(alt+'/USDT', limit=100)
            df = pd.DataFrame(bars[:-1], columns=['timestamp','open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            ist = pytz.timezone("Asia/Kolkata")
            df['timestamp']=df['timestamp'].dt.tz_localize('UTC').dt.tz_convert(ist)
            print(df[-1:])
            close_data=df['close']
            high_data=df['high']
            high_data=high_data[len(high_data)-1]
            low_data=df['low']
            low_data=low_data[len(low_data)-1]
        return alt,asks,bids,bal_stable,bal_alt,close_data,high_data,low_data