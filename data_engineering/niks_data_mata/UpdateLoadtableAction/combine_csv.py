import pandas as pd

# Load the CSV file
file_path = '/Users/nikyakovlev/Documents/GitHub/aircraft_load/data_engineering/niks_data_mata/UpdateLoadtableAction/unique_extracted_totals_ABCD_MNOP.csv'
df = pd.read_csv(file_path)

# List of columns to remove
columns_to_remove = ['total_eic', 'total_mnc', 'total_baggage']

# Drop the specified columns
df.drop(columns=columns_to_remove, inplace=True, errors='ignore')

# Save the modified DataFrame to a new CSV file
output_file_path = '/Users/nikyakovlev/Documents/GitHub/aircraft_load/data_engineering/niks_data_mata/UpdateLoadtableAction/unique_extracted_totals_ABCD_MNOP_.csv'
df.to_csv(output_file_path, index=False)

print("Columns removed and the file has been saved to", output_file_path)
