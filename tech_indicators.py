import pyta
from fetch_data_from_exchange import FetchData

class TechIndicators:
    def __init__(self) -> None:
        self.fetch_data = FetchData()

    def rsi_BBand(self):
        alt = self.fetch_data.fetch_data_from_exchange()[0]
        close_val = self.fetch_data.fetch_data_from_exchange()[5]
        rsi = pyta.RSI(close_val)
        rsi=rsi[len(rsi)-1]
        print('RSI of '+ alt + ' = '+ str(rsi))
        upper, middle, lower = pyta.BBANDS(close_val)
        upper=upper[len(upper)-1]
        middle=middle[len(middle)-1]
        lower=lower[len(lower)-1]
        print('Upper : '+ str(upper),'Middle : ' + str(middle),'Lower : '+ str(lower))
        return rsi, upper, middle, lower