import pandas as pd

# filter data for action: GetCabinConfigurationsAction
data = pd.read_parquet('../data/data_parquet/processed_data_combined.parquet')
action_data = data[data['action_name'] == 'GetCabinConfigurationsAction']
print(action_data.head())
