# import necessary libraries
import pandas as pd
import os

# define the path to the processed data file
processed_data_path_aref = '/Users/arefhasan/Documents/uni_proejcts/aircraft_load/data/data_parquet/processed_data_combined.parquet' # please change the path if you want to run this file

# load the concatenated data
data = pd.read_parquet(processed_data_path_aref)

# define the directory to save the action files
actions_dir = '../aircraft_load/data_engineering/actions/todo'

# create the directory if it doesn't exist
if not os.path.exists(actions_dir):
    os.makedirs(actions_dir)

# get unique actions from the action_name column
unique_actions = data['action_name'].unique()

processed_data_path = '../data/data_parquet/processed_data_combined.parquet'
# create a separate Python file for each unique action
for action in unique_actions:
    action_filename = f'{actions_dir}/{action}.py'
    
    # remove the existing file if it exists
    if os.path.isfile(action_filename):
        os.remove(action_filename)
    
    # create a new file with minimal content
    with open(action_filename, 'w') as file:
        file.write(f"import pandas as pd\n\n")
        file.write(f"# filter data for action: {action}\n")
        file.write(f"data = pd.read_parquet('{processed_data_path}')\n")
        file.write(f"action_data = data[data['action_name'] == '{action}']\n")
        file.write(f"print(action_data.head())\n")
