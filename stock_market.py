import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

import yfinance as yf

# Download data for Apple (AAPL)
aapl = yf.Ticker("AAPL")

# Get historical data for the last 5 years
hist = aapl.history(period="5y")

# Print the data
print(hist)
print(hist.head())
