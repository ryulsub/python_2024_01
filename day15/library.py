# library

# import yfinance
#
# apple = yfinance.Ticker("AAPL")
# current_price = apple.info['currentPrice']
# print(f"애플 주식의 현재 가격: {current_price}")

#import cctx
# ticker = exchange.fetch_ticker('BTC/USD')
# current_price = ticker['last']
# print(f"BTC/USD의 현재 가격: {current_price}")
#exchange = cctx.binance()

import yfinance

microsoft = yfinance.Ticker("MSFT")
current_price = microsoft.info['currentPrice']
print(f"마이크로 소프트 주식의 현재 가격: {current_price}")