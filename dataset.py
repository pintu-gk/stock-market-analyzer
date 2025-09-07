import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Combined_News_DJIA.csv")


data["Date"] = pd.to_datetime(data["Date"])


plt.figure(figsize=(12,6))
plt.plot(data["Date"], data["Close"], label="Closing Price", color="blue")
plt.xlabel("Date")
plt.ylabel("Stock Close Price")
plt.title("Stock Market Closing Price Over Time")
plt.legend()
plt.grid(True)
plt.show()
