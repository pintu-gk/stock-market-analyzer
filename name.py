import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Combined_News_DJIA.csv')
df1=pd.read_csv('RedditNews.csv')
df2=pd.read_csv('upload_DJIA_table.csv')
print(df.head())
print(df1.head())
print(df2.head())
print(df)
print(df1)
print(df2)
print(df.columns)
print(df.rpow)
print(df2.columns)
print(df2.rpow)

plt.figure(figsize=(2,6))
plt.title('stock market')
plt.xlabel('jkghkj')
plt.ylabel('iug')



plt.show()


print(df.shape)