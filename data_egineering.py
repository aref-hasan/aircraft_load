import pandas as pd

# original data
data = pd.read_csv('../aircraft_load/data/raw_data.csv', sep=';')

# copy of DataFrame
modified_data = data.copy()

# Convert 'creation_time' to datetime & correct the format
modified_data['creation_time'] = pd.to_datetime(modified_data['creation_time'], format='%Y-%m-%dT%H:%M:%S.%f')

# Format date
modified_data['formatted_creation_time'] = modified_data['creation_time'].dt.strftime('%d-%m-%Y %H:%M:%S')

# new CSV file
output_path = '../aircraft_load/data/modified_data.csv'

# Save modified DataFrame 
modified_data.to_csv(output_path, index=False)  # Set 'index=False' to avoid writing row numbers to the file
