import re
from typing import Optional
def UpdateEstimatesAction(string) -> Optional[int]:
    pattern = r"EZFW\s*:\s*(\d+(?:\.\d*)?)\s*KG"

    match = re.search(pattern, string)
    if match:
        estimate_zfw = int(float(match.group(1)))
        return estimate_zfw
