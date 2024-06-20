import pandas as pd

# america
file_path = './data/data_samples/america_5_flights.csv'

df = pd.read_csv(file_path)

df = df.drop(columns=['entry_details'])
df = df.drop(columns=['airline_code'])
df = df.drop(columns=['header_line'])
df = df.drop(columns=['user_name'])

df.to_csv('./data/drop_entry-details/america_5_flights_drop_entry.csv', index=False)


# asia
file_path = './data/data_samples/asia_5_flights.csv'

df = pd.read_csv(file_path)

df = df.drop(columns=['entry_details'])
df = df.drop(columns=['airline_code'])
df = df.drop(columns=['header_line'])
df = df.drop(columns=['user_name'])

df.to_csv('./data/drop_entry-details/asia_5_flights_drop_entry.csv', index=False)


# europe
file_path = './data/data_samples/europe_5_flights.csv'

df = pd.read_csv(file_path)

df = df.drop(columns=['entry_details'])
df = df.drop(columns=['airline_code'])
df = df.drop(columns=['header_line'])
df = df.drop(columns=['user_name'])

df.to_csv('./data/drop_entry-details/europe_5_flights_drop_entry.csv', index=False)