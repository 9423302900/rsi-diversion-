import schedule
import time
from data.fetch_price import get_ohlc
from strategy.rsi_divergence import detect_rsi_divergence
from alerts.telegram import send_telegram_alert
from alerts.google_logger import log_to_sheet

symbols = [
    "RELIANCE.NS", "TATAMOTORS.NS", "SBIN.NS", "ICICIBANK.NS", "AXISBANK.NS", "INFY.NS", "WIPRO.NS", "HDFCBANK.NS",
    "HCLTECH.NS", "TECHM.NS", "ADANIENT.NS", "ADANIPORTS.NS", "BPCL.NS", "TATAPOWER.NS", "ONGC.NS", "ITC.NS",
    "MARUTI.NS", "TATASTEEL.NS", "JSWSTEEL.NS", "GRASIM.NS", "ULTRACEMCO.NS", "CIPLA.NS", "SUNPHARMA.NS", "DIVISLAB.NS",
    "COALINDIA.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", "EICHERMOT.NS", "LT.NS", "CROMPTON.NS", "CRUDEOIL.NS"
]

def run_scan():
    for symbol in symbols:
        try:
            df = get_ohlc(symbol)
            signal = detect_rsi_divergence(df)

            if signal:
                price = df['close'].iloc[-1]
                msg = f"🔔 {signal} Signal on {symbol} | Price: ₹{round(price, 2)}"
                send_telegram_alert(msg)
                log_to_sheet(symbol, signal, round(price, 2))
                print(msg)
        except Exception as e:
            print(f"Error processing {symbol}: {e}")

schedule.every(15).minutes.do(run_scan)

while True:
    schedule.run_pending()
    time.sleep(1)
