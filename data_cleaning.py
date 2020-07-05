import pandas as pd

df = pd.read_csv('carprice_scraper/output/carmudi-dataset.csv') 

df['location'] = df['location'].apply(lambda x: x.strip('\n'))
df['odometer'] = df['odometer'].apply(lambda x: x.strip('Km'))
df['price'] = df['price'].apply(lambda x: x.strip('Juta'))

df_out = df
df_out.to_csv('carmudi_data_cleaned.csv', index=False)
