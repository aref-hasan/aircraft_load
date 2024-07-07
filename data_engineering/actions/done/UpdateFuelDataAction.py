import re
from typing import Optional
def UpdateFuelDataAction(string) -> Optional[int]:
    take_off_fuel = None
    minimum_tof = None
    pattern = r'Take Off Fuel\s*:\s*([\d.]+) KG'
    match = re.search(pattern, string)
    if match:
        take_off_fuel = int(float(match.group(1)))
    
    
    pattern = r'Minimum TOF\s*:\s*([\d.]+) KG'
    match = re.search(pattern, string)
    if match:
        minimum_tof = int(float(match.group(1)))
    return take_off_fuel, minimum_tof

