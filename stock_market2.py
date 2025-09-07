import yfinance as yf
import mplfinance as mpf

# Apple  data download
aapl = yf.Ticker("AAPL")
#range of date to convert a candal form
df = aapl.history(start="2025-01-01", end="2025-9-05")




# Candlestick chart plot
mpf.plot(
    df,
    type="candle",       # candle form 
    style="yahoo",       # styling  a sty format (yahoo, charles, classic, etc...)
    title="Apple Stock Price",
    ylabel="Price ($)",
    ylabel_lower="Volume",
    volume=True          # volume chart to down are show
)
