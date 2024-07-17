import pandas as pd
import re

def extract_totals_from_details(text):
    # Define the regex pattern to capture totals from the text
    totals_pattern = re.compile(
        r"Total cargo\s*:\s*(?P<total_cargo>[\d\.]+)\s*KG\s*"
        r"Total EIC\s*:\s*(?P<total_eic>[\d\.]+)\s*KG\s*"
        r"Total mail\s*:\s*(?P<total_mail>[\d\.]+)\s*KG"
    )
    # Search for the pattern
    match = totals_pattern.search(text)
    return match.groupdict() if match else {"total_cargo": None, "total_eic": None, "total_mail": None}

# Load your CSV file
file_path = '../data_engineering/UpdateLoadtableAction/UpdateLoadTableAction_entries_ZYXW.csv'  # Update this path to your CSV file location
df = pd.read_csv(file_path)

# Apply the function to extract totals from the 'entry_details' column
df_totals = df['entry_details'].apply(extract_totals_from_details)

# Convert the series of dictionaries to a DataFrame
baggage_data_df = pd.DataFrame(list(df_totals))

# Include the additional columns
df['timestamp'] = df['creation_time']
df['creation_time'] = pd.to_datetime(df['creation_time']).dt.to_period('M').astype(str)
df['creation_time'] = df['creation_time'].str.replace('-04', '-05')
df['combined'] = df['creation_time'] + '_' + df['airline_code'] + '_' + df['flight_number'].astype(str) + '_' + df['flight_date'].astype(str)

# Add the departure airport column to the baggage_data_df
baggage_data_df['departure_airport'] = df['departure_airport']

# Add the combined column and timestamp to the baggage_data_df
baggage_data_df['combined'] = df['combined']
baggage_data_df['timestamp'] = df['timestamp']

# Display the first few rows of the final DataFrame
print(baggage_data_df.head())

# Save the final DataFrame to a new CSV file
output_file_path = '../data_engineering/UpdateLoadtableAction/extracted_totals_ZYXW.csv'  # Update this path to where you want to save the new CSV
baggage_data_df.to_csv(output_file_path, index=False)


################################################

# Load the CSV file
file_path = '../data_engineering/UpdateLoadtableAction/extracted_totals_ZYXW.csv'  # Update this path to your CSV file location
df = pd.read_csv(file_path)

# Ensure that timestamp is a datetime object for proper sorting
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Filter rows where all three totals are not null
df_filtered = df.dropna(subset=['total_cargo', 'total_eic', 'total_mail'])

# Sort by 'timestamp' and 'combined', then drop duplicates keeping the last (most recent) entry for each 'combined'
df_latest = df_filtered.sort_values(by='timestamp').drop_duplicates('combined', keep='last')

# Save the final DataFrame to a new CSV file
output_file_path = '../data_engineering/UpdateLoadtableAction/unique_extracted_totals_ZYXW.csv'  # Update this path to where you want to save the new CSV
df_latest.to_csv(output_file_path, index=False)

# Display the first few rows of the final DataFrame to verify the output
print(df_latest.head())
