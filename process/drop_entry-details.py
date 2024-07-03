import pandas as pd

# Funktion zum Laden und Bearbeiten der CSV-Datei
def process_csv(file_path, output_path):
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip')
        df = df.drop(columns=['entry_details', 'airline_code', 'header_line', 'user_name'])
        df.to_csv(output_path, index=False)
    except pd.errors.ParserError as e:
        print(f"Fehler beim Parsen der Datei {file_path}: {e}")

# ABCD
file_path = '/Users/lucamohr/GitHub/aircraft_load/data/original_data/ABCD_tripfiles.csv'
output_path = '/Users/lucamohr/GitHub/aircraft_load/data/drop_entry-details/ABCD_tripfiles_drop_entry.csv'
process_csv(file_path, output_path)

# MNOP
file_path = '/Users/lucamohr/GitHub/aircraft_load/data/original_data/MNOP_tripfiles.csv'
output_path = '/Users/lucamohr/GitHub/aircraft_load/data/drop_entry-details/MNOP_tripfiles_drop_entry.csv'
process_csv(file_path, output_path)

# ZYXW
file_path = '/Users/lucamohr/GitHub/aircraft_load/data/original_data/ZYXW_tripfiles.csv'
output_path = '/Users/lucamohr/GitHub/aircraft_load/data/drop_entry-details/ZYXW_tripfiles_drop_entry.csv'
process_csv(file_path, output_path)
