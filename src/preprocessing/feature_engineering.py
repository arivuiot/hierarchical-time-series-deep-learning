import numpy as np, pandas as pd
def features(df):
 df['lag1']=df.groupby(['region','store','sku'])['sales'].shift(1)
 df['lag7']=df.groupby(['region','store','sku'])['sales'].shift(7)
 df['rmean7']=df.groupby(['region','store','sku'])['sales'].shift(1).rolling(7).mean()
 df['time_sin']=np.sin(2*np.pi*df['time']/12)
 return df.dropna()
