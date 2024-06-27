# import necessary libraries
import pandas as pd
import os
import importlib.util

# define the path to the processed data file
processed_data_path = '/Users/arefhasan/Documents/uni_proejcts/aircraft_load/data/data_parquet/processed_data_combined.parquet'
weights_data_path = '/Users/arefhasan/Documents/uni_proejcts/aircraft_load/data/data_parquet/weights_data.csv'
# load the concatenated data
data = pd.read_parquet(processed_data_path)

# filter the data for the specific flight number
filtered_data = data[data['flight_number'] == 2127]

# count the number of rows for each action_mode
counts = filtered_data['action_mode'].value_counts()

print("Number of rows for each action_mode in flight 2127:")
print(counts)

# define the columns for the weights DataFrame
weight_columns = [
    'flight_number', 'formatted_creation_time', 'stepID', 
    'dry_operating_weight', 'estim_total_traffic_load', 'actual_zfw', 
    'basic_weight', 'basic_index', 'ZFW', 'STATUS', 'LOADSHEET', 
    'LOADING_INSTRUCTION', 'FUEL', 'AIRCRAFT_CONFIG', 'EZFW', 
    'CARGO_FINAL', 'RAMP_FINAL', 'CHECK_IN_FINAL', 'CARGO_TRANSFER', 
    'OFP', 'CABIN_CONFIG', 'AUTO_MODE_ACTIVE', 'AUTOMATION_STARTED', 
    'BAG_LOAD_ITEMS_GEN', 'EZFW_COUNTER', 'REGISTRATION', 
    'REGISTRATION_CHANGE', 'FUEL_ORDER'
]

# create an empty DataFrame for the weights
weights_data = pd.DataFrame(columns=weight_columns)

# define the directory where the action files are saved
actions_dir = '../aircraft_load/data_engineering/actions'

# create a dictionary to cache the imported modules
imported_modules = {}

# function to save the weights data periodically
def save_weights_data_csv(weights_data, path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    weights_data.to_csv(path, index=False)
    print(f"Weights data saved to {path}")

# iterate through each row in the filtered dataset
for index, row in filtered_data.iterrows():
    action = row['action_name']
    
    if action == "CreateZFWMessageAction":
        action_filename = f'{actions_dir}/{action}.py'
        
        if os.path.isfile(action_filename):
            if action not in imported_modules:
                # import the action module and cache it
                module_name = f'{action}_module'
                spec = importlib.util.spec_from_file_location(module_name, action_filename)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                imported_modules[action] = module
            else:
                module = imported_modules[action]
            
            # execute the action module and extract weight information
            weight_info = module.extract_weight_info(row)  # assuming each action file has a function called extract_weight_info
            if weight_info:
                # add additional fields from the main dataset
                weight_info.update({
                    'flight_number': row['flight_number'],
                    'formatted_creation_time': row['formatted_creation_time'],
                    'stepID': row['stepID']
                })
                weights_data = pd.concat([weights_data, pd.DataFrame([weight_info])], ignore_index=True)
            else:
                print(f"Weight info is None for row {index}")
        else:
            print(f'No action file found for {action}')
    else:
        print(f"Skipping action {action} for row {index}")
    
    # periodically save the weights data
    if index % 100 == 0:  # adjust the saving frequency as needed
        save_weights_data_csv(weights_data, weights_data_path)

# save the final weights data
save_weights_data_csv(weights_data, weights_data_path)

# check the results
print(weights_data.head())