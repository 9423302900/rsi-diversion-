
from data.fetch_price import get_ohlc
from strategy.rsi_divergence import detect_rsi_divergence
from alerts.telegram import send_telegram_alert

symbols = ["RELIANCE.NS", "TATAMOTORS.NS", "SBIN.NS", "INFY.NS", "CRUDEOIL.NS"]

for symbol in symbols:
    df = get_ohlc(symbol)
    signal = detect_rsi_divergence(df)

    if signal:
        msg = f"🔔 {signal} Signal Detected on {symbol}\nPrice: {df['close'].iloc[-1]}"
        send_telegram_alert(msg)
        print(msg)
