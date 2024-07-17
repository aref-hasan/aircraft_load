import pandas as pd

# Load the CSV files
file_path_cargo = '/Users/nikyakovlev/Documents/GitHub/aircraft_load/data_engineering/niks_data_mata/UpdateEstimatesAction/cargo_estimates_MNOP_ABCD.csv'
file_path_extracted = '/Users/nikyakovlev/Documents/GitHub/aircraft_load/data_engineering/niks_data_mata/UpdateLoadtableAction/unique_extracted_totals_ABCD_MNOP.csv'

df_cargo = pd.read_csv(file_path_cargo)
df_extracted = pd.read_csv(file_path_extracted)

# Merge the DataFrames on the 'combined' column using an inner join
result_df = pd.merge(df_cargo, df_extracted, on='combined', how='inner')

# Save the merged DataFrame to a new CSV file
output_file_path = '/Users/nikyakovlev/Documents/GitHub/aircraft_load/data_engineering/niks_data_mata/UpdateEstimatesAction/cargo_estimates_and_loadtable_MNOP_ABCD.csv'
result_df.to_csv(output_file_path, index=False)

print("Data merged successfully and saved to", output_file_path)
