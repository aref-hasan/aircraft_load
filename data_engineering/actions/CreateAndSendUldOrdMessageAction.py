import pandas as pd

# filter data for action: CreateAndSendUldOrdMessageAction
data = pd.read_parquet('../data/data_parquet/processed_data_combined.parquet')
action_data = data[data['action_name'] == 'CreateAndSendUldOrdMessageAction']
print(action_data.head())
