import re
from typing import Optional

def UpdateEstimatesAction(string: str) -> Optional[int]:
    """
    Parses the input string to extract the estimated zero fuel weight (EZFW) value in kilograms.

    Args:
        string (str): The input string containing the EZFW value in the format 'EZFW : <value> KG'.

    Returns:
        Optional[int]: The estimated zero fuel weight as an integer if found, otherwise None.
    """
    pattern = r"EZFW\s*:\s*(\d+(?:\.\d*)?)\s*KG"

    match = re.search(pattern, string)
    if match:
        estimate_zfw = int(float(match.group(1)))
        return estimate_zfw

    return None