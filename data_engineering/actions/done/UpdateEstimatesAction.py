import pandas as pd
import re

def extract_cargo_mail_weights(text):
    # define the regex pattern to capture cargo and mail weights from the text
    weights_pattern = re.compile(
        r"Cargo\s*:\s*(?P<cargo_weight>[\d\.]+)\s*KG\s*"
        r"Mail\s*:\s*(?P<mail_weight>[\d\.]+)\s*KG"
    )
    # search for the pattern
    match = weights_pattern.search(text)
    return match.groupdict() if match else {"cargo_weight": None, "mail_weight": None}

# load the provided CSV file
file_path = '/data_engineering/UpdateEstimatesAction/UpdateEstimatesAction_entries_ZYXW.csv'
df = pd.read_csv(file_path)

# apply the function to extract cargo and mail weights from the 'entry_details' column
df_weights = df['entry_details'].apply(extract_cargo_mail_weights)

# convert the series of dictionaries to a DataFrame
weights_data_df = pd.DataFrame(list(df_weights))

# create the 'timestamp' column as a direct copy of 'creation_time'
weights_data_df['timestamp'] = pd.to_datetime(df['creation_time'])

# create the 'combined' column, including transformation of date
df['creation_time'] = pd.to_datetime(df['creation_time']).dt.to_period('M').astype(str)
df['creation_time'] = df['creation_time'].str.replace('-04', '-05')
weights_data_df['combined'] = df['creation_time'] + '_' + df['airline_code'] + '_' + df['flight_number'].astype(str) + '_' + df['flight_date'].astype(str)

# ensure only entries with valid cargo and mail weights are considered
weights_data_df = weights_data_df.dropna(subset=['cargo_weight', 'mail_weight'])

# sort by 'timestamp' to ensure the latest entries are at the top
weights_data_df = weights_data_df.sort_values(by='timestamp', ascending=False)

# drop duplicates keeping only the first entry which is the latest due to sort
weights_data_df = weights_data_df.drop_duplicates(subset='combined', keep='first')

# first few rows of the final DataFrame
print(weights_data_df.head())

# DataFrame to a new CSV file
output_file_path = '../data/UpdateEstimatesAction/cargo_estimates_ZYXW.csv'
weights_data_df.to_csv(output_file_path, index=False)
