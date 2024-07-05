# import necessary libraries
import pandas as pd
import json

def load_config(path):
    with open(path, 'r') as file:
        return json.load(file)

config_path = '../pandas_config.json'
config = load_config(config_path)
parquet_config = config['parquet']

# setting up the engine as a global constant
ENGINE = parquet_config['engine']
COMPRESSION = parquet_config['compression']
FILE_PATH = "../data"

file1 = FILE_PATH + "/asia_data.csv"
file2 = FILE_PATH + "/europe_data.csv"
file3 = FILE_PATH + "/america_data.csv"
parquet_file1 = FILE_PATH + "/data_parquet/asia_data.parquet"
parquet_file2 = FILE_PATH + "/data_parquet/europe_data.parquet"
parquet_file3 = FILE_PATH + "/data_parquet/america_data.parquet"


df = pd.read_csv(file1, on_bad_lines='skip')
df.to_parquet(parquet_file1, engine=ENGINE, compression=COMPRESSION)

df = pd.read_csv(file2, on_bad_lines='skip')
df.to_parquet(parquet_file2, engine=ENGINE, compression=COMPRESSION)

df = pd.read_csv(file3, on_bad_lines='skip')
df.to_parquet(parquet_file3, engine=ENGINE, compression=COMPRESSION)


df = pd.read_parquet(FILE_PATH + "/data_parquet/europe_data.parquet").head(1000)
df.to_csv(FILE_PATH + "/data_samples/europe_data_1000.csv")

