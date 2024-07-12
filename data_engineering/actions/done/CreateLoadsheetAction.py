import re
from typing import Optional, Tuple

def CreateLoadsheetAction(string: str) -> Tuple[Optional[int], Optional[int], Optional[int], Optional[int]]:
    actual_tow = None
    actual_zfw = None
    estimated_zfw = None
    fuel = None
    
    if string is not None:
        pattern = r"TAKE OFF WEIGHT ACTUAL\s+(\d+)"
        match_actual_tow = re.search(pattern, string)
        if match_actual_tow:
            actual_tow = int(float(match_actual_tow.group(1)))
        
        pattern = r"ZERO FUEL WEIGHT ACTUAL\s+(\d+)"
        match_actual_zfw = re.search(pattern, string)
        if match_actual_zfw:
            actual_zfw = int(float(match_actual_zfw.group(1)))


        pattern = r"TAKE OFF FUEL\s+(\d+)"
        match_fuel = re.search(pattern, string)
        if match_fuel:
            fuel = int(float(match_fuel.group(1)))

        pattern = r"ESTIMATED_ZFW\s*:\s*(\d+(?:\.\d*)?)\s*KG"
        match = re.search(pattern, string)
        if match:
            estimated_zfw = int(float(match.group(1)))
    
    return actual_tow, actual_zfw, estimated_zfw, fuel
