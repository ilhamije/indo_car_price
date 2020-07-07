import pandas as pd

df = pd.read_csv('carprice_scraper/output/carmudi-dataset.csv') 

df['brand'] = df['brand'].apply(lambda x: x.strip('\"\n '))
df['location'] = df['location'].apply(lambda x: x.strip('\n'))
df['price'] = df['price'].apply(lambda x: x.strip('Juta'))

df['odometer'] = df['odometer'].apply(lambda x: x.strip(' Km'))
df['odometer'] = df['odometer'].str.replace(',', '').astype(float)
df['odometer'] = pd.to_numeric(df['odometer'])

df_out = df
df_out.to_csv('carmudi_data_cleaned.csv', index=False)
