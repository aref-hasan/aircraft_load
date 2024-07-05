import pandas as pd
import os

datei = '../process/data/data_csv/combined_data.csv'
df = pd.read_csv(datei)

df_ersten_1000 = df.head(1000)

zielverzeichnis = '../process/data/data_csv'

os.makedirs(zielverzeichnis, exist_ok=True)

neue_datei = os.path.join(zielverzeichnis, 'combined_data_1000.csv')

df_ersten_1000.to_csv(neue_datei, index=False)

print(df_ersten_1000.head())