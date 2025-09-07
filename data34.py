import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf



print("Creating a sample stock data DataFrame...")
dates = pd.date_range(start='2025-01-07', periods=100, freq='D')
np.random.seed(42) # For reproducibility
prices = np.random.normal(loc=150, scale=5, size=100).cumsum() + 100
df = pd.DataFrame({'Date': dates, 'Close': prices})
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
print("Sample DataFrame created successfully.")
print(df.head())
print("-" * 50)

# -----------------------------------------------------------------------------
# Step 2: Calculate a Simple Moving Average (SMA)
# SMA ek basic financial indicator hai. Ye pichle 'n' dino ki
# average price ko calculate karta hai. Hum yahan 20-day SMA calculate karenge.
# -----------------------------------------------------------------------------
window = 20
print(f"Calculating {window}-day Simple Moving Average (SMA)...")
df['SMA_20'] = df['Close'].rolling(window=window).mean()
print("SMA calculated successfully.")
print(df.tail())
print("-" * 50)

# -----------------------------------------------------------------------------
# Step 3: Visualize the Data
# Matplotlib ka upyog karke stock prices aur SMA ko plot karenge
# taaki hum trends ko dekh sakein.
# -----------------------------------------------------------------------------
print("Generating the plot...")
plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(12, 6))

# Plot the stock's closing price
plt.plot(df.index, df['Close'], label='Closing Price', color='skyblue', linewidth=2)

# Plot the Simple Moving Average
plt.plot(df.index, df['SMA_20'], label=f'{window}-Day SMA', color='orange', linestyle='--', linewidth=2)

# Add title and labels
type='candle',
style="yahoo",
plt.title('Stock Price and 20-Day Simple Moving Average', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Plot displayed. Program finished.")
