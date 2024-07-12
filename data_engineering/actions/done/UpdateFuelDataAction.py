import re
from typing import Optional, Tuple

def UpdateFuelDataAction(string: str) -> Tuple[Optional[int], Optional[int]]:
    """
    Parses the input string to extract the take off fuel and minimum take off fuel (TOF) values in kilograms.

    Args:
        string (str): The input string containing the fuel values in the format
                      'Take Off Fuel : <value> KG' and 'Minimum TOF : <value> KG'.

    Returns:
        Tuple[Optional[int], Optional[int]]:
            - take_off_fuel: The take off fuel as an integer if found, otherwise None.
            - minimum_tof: The minimum take off fuel as an integer if found, otherwise None.
    """
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