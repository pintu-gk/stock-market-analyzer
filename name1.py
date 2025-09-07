import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Combined_News_DJIA.csv')
df1=pd.read_csv('RedditNews.csv')
df2=pd.read_csv('upload_DJIA_table.csv')
plt.figure(figsize=(8,3)) 
slote = pd.to_datetime(df2['Date'])

plt.plot(slote, color='blue')

plt.xlabel("stock price ")
plt.ylabel("year")
plt.title("Stock Market Closing Price Over Time")




plt.legend()
plt.grid(True)
plt.show()
print(df2)
