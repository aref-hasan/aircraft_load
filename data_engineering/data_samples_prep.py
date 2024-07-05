#### This script generates various examples from the main dataset for better understanding and analysis ####

# import necessary libraries
import pandas as pd
import re

# extract the first 1000 rows from europe_data parquet file and save as csv
df = pd.read_parquet("data/data_parquet/europe_data.parquet").head(1000)
df.to_csv("data/data_samples/europe_data_1000.csv")

# load the combined processed data and actions data
data = pd.read_parquet('data/data_parquet/processed_data_combined.parquet')
actions = pd.read_excel('data/Liste_der_Actions.xlsx')
action_names = actions["Action Name"].values

# filter the data based on action names and statuses, then save to csv
filtered_df = None
for action in action_names:
    for status in ["Received", "Saved", "Sent"]:
        if filtered_df is None:
            tempDF = data[(data["action_name"] == action) & (data["action_mode"] == status)].head(10)
            filtered_df = tempDF
        else:
            actiondf = data[(data["action_name"] == action) & (data["action_mode"] == status)].head(10)
            filtered_df = pd.concat([filtered_df, actiondf])

filtered_df.to_csv('data/actions.csv')

# generate samples of 5 flights from each continent and save as csv
continents = ["europe", "america", "asia"]
for continent in continents:
    df = pd.read_parquet(f"data/data_parquet/{continent}_data.parquet")
    flight_numbers = df["flight_number"].values
    subset_flight_numbers = flight_numbers[:5]
    five_flights = df[df["flight_number"].isin(subset_flight_numbers)]
    five_flights.to_csv(f"data/data_samples/{continent}_5_flights.csv")
