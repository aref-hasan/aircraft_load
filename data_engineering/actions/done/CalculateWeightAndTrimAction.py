import re
from typing import Optional

def CalculateWeightAndTrimAction(string: str) -> Optional[int]:
    """
    Parses the input string to extract the actual zero fuel weight (AZFW) in kilograms.

    Args:
        string (str): The input string containing the AZFW value in the format 'AZFW : <value> KG'.

    Returns:
        Optional[int]: The actual zero fuel weight as an integer if found, otherwise None.
    """
    pattern = r"AZFW\s*:\s*(\d+(?:\.\d*)?)\s*KG"

    match = re.search(pattern, string)
    if match:
        actual_zfw = int(float(match.group(1)))
        return actual_zfw
    
    return None