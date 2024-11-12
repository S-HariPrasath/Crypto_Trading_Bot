from tech_indicators import TechIndicators
from fetch_data_from_exchange import FetchData
from constants import EXCHANGE
from send_trading_report_in_mail import SendEmail

class PlaceOrders:
    def __init__(self) -> None:
        self.alt, self.ask, self.bid, self.bal_stable, self.bal_alt, _, self.high_val, self.low_val = FetchData().fetch_data_from_exchange()
        self.rsi, self.bol_upper_value, self.bol_middle_value, self.bol_lower_value = TechIndicators().rsi_BBand()
       
    def buy_order(self):
        buy_qty = self.bal_stable/self.ask
        buy_qty = round(buy_qty,4)
        print("Alt qty is "+str(buy_qty))
        buy_order = EXCHANGE.create_market_buy_order(self.alt+'/USDT', buy_qty)
        buy_msg = 'You have bought '+ str(buy_qty) + self.alt
        buy_subject = 'BUY ORDER MSG'
        SendEmail().send_email(buy_msg, buy_subject)
        return buy_order
        
    def sell_order(self):
        fetch_trade = EXCHANGE.fetch_my_trades(self.alt+'/USDT', limit=1)
        bought_qty = float((fetch_trade[0]['info']['qty']))
        bought_bid = float(fetch_trade[0]['price'])
        profit = bought_qty*self.bid-(bought_qty*bought_bid)
        sell_order = EXCHANGE.create_market_sell_order(self.alt+'/USDT', self.bal_alt)
        sell_msg = 'You have sold ' + str(self.bal_alt) + self.alt + '\nThe profit is ' + str(profit)
        sell_subject = "SOLD ORDER MSG"
        SendEmail().send_email(sell_msg, sell_subject)
        return profit, sell_order
