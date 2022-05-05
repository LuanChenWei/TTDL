import pandas as pd
import numpy as np

df = pd.read_csv('OnlineRetail.csv', encoding='ISO-8859-1')
# print(df.info())

# df['Month']=pd.to_datetime(df['InvoiceDate'],format='%Y-%m-%d %H:%M:%S').dt.month
# print(df)

#invoice month
# df = df['InvoiceDate'].str.split('/').str[0]
conditions = [(df['InvoiceDate'].str.split('/').str[0] == '1') & (df['InvoiceDate'].str.split('/').str[0] == '2') & (df['InvoiceDate'].str.split('/').str[0] == '3'),
              (df['InvoiceDate'].str.split('/').str[0] == '4') & (df['InvoiceDate'].str.split('/').str[0] == '5') & (df['InvoiceDate'].str.split('/').str[0] == '6'),
              (df['InvoiceDate'].str.split('/').str[0] == '7') & (df['InvoiceDate'].str.split('/').str[0] == '8') & (df['InvoiceDate'].str.split('/').str[0] == '9')]
choices = ['1','2','3']
df['previous'] = np.select(conditions, choices, default='4')

df['Amount'] = df['Quantity'] * df['UnitPrice']

conditions2 = [(df['Country'] == 'United Kingdom') & (df['previous'] == '4'),
               (df['Country'] == 'France')]

choices2 = ['10%','5%']

df['Discount'] = np.select(conditions2, choices2, default='0%')

# df['Total'] = df['Amount'] - df['Discount']

print(df)