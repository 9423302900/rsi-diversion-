import pandas as pd
import ta

def detect_rsi_divergence(df):
    df['RSI'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()

    lows = df.iloc[-20:].nsmallest(2, 'close')
    highs = df.iloc[-20:].nlargest(2, 'close')

    signal = None
    if lows.shape[0] == 2:
        low1, low2 = lows.iloc[0], lows.iloc[1]
        if low1['close'] > low2['close'] and low1['RSI'] < low2['RSI']:
            signal = "BUY"
    if highs.shape[0] == 2:
        high1, high2 = highs.iloc[0], highs.iloc[1]
        if high1['close'] < high2['close'] and high1['RSI'] > high2['RSI']:
            signal = "SELL"

    return signal
