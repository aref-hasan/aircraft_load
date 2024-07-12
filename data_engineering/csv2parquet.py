import pandas as pd
import json
import os

# Function to load configuration from a json file
def load_config(path: str):
    with open(path, 'r') as file:
        return json.load(file)

# Load configuration for Parquet settings
config_path = '../pandas_config.json'
config = load_config(config_path)
parquet_config = config['parquet']

# Setting up the engine and compression as global constants
ENGINE = parquet_config['engine']
COMPRESSION = parquet_config['compression']
FILE_PATH = "../data"

# Define file paths for CSV and Parquet files
file1 = FILE_PATH + "/asia_data.csv"
file2 = FILE_PATH + "/europe_data.csv"
file3 = FILE_PATH + "/america_data.csv"
parquet_dir1 = FILE_PATH + "/data_parquet/asia"
parquet_dir2 = FILE_PATH + "/data_parquet/europe"
parquet_dir3 = FILE_PATH + "/data_parquet/america"

# Function to read CSV in chunks and save as Parquet
def read_and_save_in_chunks(csv_file, parquet_dir, file_prefix, chunk_size=500000):
    if not os.path.exists(parquet_dir):
        os.makedirs(parquet_dir)
    chunk_iter = pd.read_csv(csv_file, chunksize=chunk_size, on_bad_lines='skip')
    for i, chunk in enumerate(chunk_iter):
        chunk.to_parquet(f"{parquet_dir}/{file_prefix}_part{i+1}.parquet", engine=ENGINE, compression=COMPRESSION)

# Process each CSV file and save in chunks
read_and_save_in_chunks(file1, parquet_dir1, "asia_data")
read_and_save_in_chunks(file2, parquet_dir2, "europe_data")
read_and_save_in_chunks(file3, parquet_dir3, "america_data")

# Read the first 1000 rows from the first Europe Parquet chunk and save as CSV
first_chunk_path = f"{parquet_dir2}/europe_data_part1.parquet"
df = pd.read_parquet(first_chunk_path).head(1000)
samples_dir = FILE_PATH + "/data_samples"
if not os.path.exists(samples_dir):
    os.makedirs(samples_dir)
df.to_csv(f"{samples_dir}/europe_data_1000.csv")