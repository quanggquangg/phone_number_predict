import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv('D:/KPDL/train_dataset.csv')
values1 = df[df["price_vnd"]>=10000000]["price_vnd"].value_counts()
values2 = df[df["price_vnd"]<10000000]["price_vnd"].value_counts()
# print(values1, values2)

price_range = []
for i in df["price_vnd"]:
    check_range = 0
    if (i <= 450000):
        check_range = 1
    elif (i == 500000):
        check_range = 2
    elif (i == 1000000):
        check_range = 3
    elif (i == 3000000):
        check_range = 4
    elif (i == 5000000):
        check_range = 5
    else: 
        check_range = 0
    price_range.append(check_range)
df['sim_price_range'] = price_range
df = df[df['sim_price_range'] == 0 ]
print(df)
df.to_csv(r'D:\KPDL\train_dataset_big.csv')