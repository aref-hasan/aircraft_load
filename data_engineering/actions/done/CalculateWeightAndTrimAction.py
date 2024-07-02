import re
from typing import Optional
def CalculateWeightAndTrimAction(string) -> Optional[int]:
    pattern = r"AZFW\s*:\s*(\d+(?:\.\d*)?)\s*KG"

    match = re.search(pattern, string)
    if match:
        actual_zfw = int(float(match.group(1)))
        return actual_zfw
