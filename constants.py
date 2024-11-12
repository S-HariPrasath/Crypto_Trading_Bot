import ccxt
import config

EXCHANGE = ccxt.binance({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY,
    "adjustForTimeDifference": True,
    "recvWindow": 10000,
})
BAL_ALT=['BTC','ETH','INJ']

