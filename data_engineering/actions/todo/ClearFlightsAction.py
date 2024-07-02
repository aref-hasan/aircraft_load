import pandas as pd

# filter data for action: ClearFlightsAction
data = pd.read_parquet('../data/data_parquet/processed_data_combined.parquet')
action_data = data[data['action_name'] == 'ClearFlightsAction']
print(action_data.head())
