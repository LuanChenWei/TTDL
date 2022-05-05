import pandas as pd


df = pd.read_excel('house_price_dống-da.xlsx')

# print(df.info())

# df1 = df[df['ward_name'] == 'Phường Trung Liệt']
# df2 = df[df['ward_name'] == 'Phường Khâm Thiên']
# print(df.head())

# df3 = df[(df['land_certificate'] == 'Sổ đỏ') & (df['bedroom'] >= 3)].filter(['area','price','house_direction','balcony_direction'])

# df4 = df.groupby('type_of_land')['price'].mean()
# df5 = df.groupby('type_of_land')['price'].max()
# df6 = df.groupby('type_of_land')['price'].min()

# df7 = df.groupby('ward_name')[['toilet','bedroom','floor']].mean()
# print(df7)