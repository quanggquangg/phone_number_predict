import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:/KPDL/t.csv')

price_vnd = []
for i in df['sim_price_range']:
    price = 0
    if (i == 1) :
        price = 450000
    elif (i ==  2):
        price = 500000
    elif (i == 3):
        price = 1000000
    elif (i == 4):
        price = 3000000
    elif (i == 5):
        price = 5000000
    price_vnd.append(price)
df['price_vnd'] = price_vnd

b = pd.read_csv('D:/KPDL/big_test.csv')

newdf = df.merge(b, how='left',on = 'sim_number')

newdf['price_vnd_y'] = newdf['price_vnd_y'].replace(np.nan, 0)


newdf['price_vnd'] = newdf['price_vnd_y'] + newdf['price_vnd_x']
print(newdf)
newdf.to_csv(r'D:\KPDL\final_result_predict.csv')