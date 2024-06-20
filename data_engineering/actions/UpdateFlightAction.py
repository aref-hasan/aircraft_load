import pandas as pd

# filter data for action: UpdateFlightAction
data = pd.read_parquet('../data/data_parquet/processed_data_combined.parquet')
action_data = data[data['action_name'] == 'UpdateFlightAction']
print(action_data.head())
