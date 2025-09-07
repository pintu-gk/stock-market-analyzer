import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf



Microsoft = yf.Ticker("MSFT")
hist=Microsoft.history(start="2025-01-03",end="2025-02-06")
print(hist)
   


mpf.plot(
    hist,
    type="candle", 
    style = mpf.make_mpf_style(base_mpf_style='nightclouds', 
                           marketcolors=mpf.make_marketcolors(up='green', down='red', wick='white',edge='black',volume='blue')),
    
    
     
  

    title="microsoft stock market candle graph",
    ylabel="Price ($)",
    ylabel_lower="Volume",
    #figursize=(12,8),
    volume=True         
)