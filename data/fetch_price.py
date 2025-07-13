import yfinance as yf

def get_ohlc(symbol, interval="15m", period="5d"):
    df = yf.download(tickers=symbol, interval=interval, period=period)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']].rename(columns=str.lower)
    return df
