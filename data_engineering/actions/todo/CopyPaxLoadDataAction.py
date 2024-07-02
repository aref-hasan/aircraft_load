import pandas as pd

# filter data for action: CopyPaxLoadDataAction
data = pd.read_parquet('../data/data_parquet/processed_data_combined.parquet')
action_data = data[data['action_name'] == 'CopyPaxLoadDataAction']
print(action_data.head())
