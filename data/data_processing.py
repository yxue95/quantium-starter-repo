import pandas as pd

df1 = pd.read_csv('daily_sales_data_0.csv')
df2 = pd.read_csv('daily_sales_data_1.csv')
df3 = pd.read_csv('daily_sales_data_2.csv')

df1 = df1[df1['product'] == 'pink morsel']
df2 = df2[df2['product'] == 'pink morsel']
df3 = df3[df3['product'] == 'pink morsel']

df1['price'] = df1['price'].replace('[\$,]', '', regex=True).astype(float)
df2['price'] = df2['price'].replace('[\$,]', '', regex=True).astype(float)
df3['price'] = df3['price'].replace('[\$,]', '', regex=True).astype(float)

df1['sales'] = df1['price'] * df1['quantity']
df2['sales'] = df2['price'] * df2['quantity']
df3['sales'] = df3['price'] * df3['quantity']


df1 = df1.drop(['product', 'price', 'quantity'], axis=1)
df2 = df2.drop(['product', 'price', 'quantity'], axis=1)
df3 = df3.drop(['product', 'price', 'quantity'], axis=1)

df = pd.concat([df1, df2, df3], ignore_index=True)

df = df.groupby(['date', 'region'], as_index=False)['sales'].sum()

df.to_csv('print_morsels.csv', index=False)


