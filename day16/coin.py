import ccxt

exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USD')
current_price = ticker['last']
prev_price = current_price

while True:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USD')
    current_price = ticker['last']
    print(f"현재 가격:{current_price}")
    if prev_price - current_price > 0:
        print("제발 도망챠")

    print(f"BTC/USD의 현재 가격: {current_price}")
    # 1$ 오르면 한강뷰 가즈아
    # 1$ 떨어지면 도망챠

