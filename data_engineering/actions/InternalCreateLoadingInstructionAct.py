import pandas as pd

# filter data for action: InternalCreateLoadingInstructionAct
data = pd.read_parquet('../data/data_parquet/processed_data_combined.parquet')
action_data = data[data['action_name'] == 'InternalCreateLoadingInstructionAct']
print(action_data.head())
