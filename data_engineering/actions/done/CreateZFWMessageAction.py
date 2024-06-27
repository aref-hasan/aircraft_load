import re
from typing import Tuple, Optional

def CreateZFWMessageAction(string: str) -> Tuple[Optional[int], Optional[int]]:
    pattern_estimated = r"^ZFW (\d+) KG"
    pattern_actual = r"<actualZFW>\s*(\d+)\s*</actualZFW>"

    estimated_zfw = None
    actual_zfw = None

    match_estimated = re.match(pattern_estimated, string)
    if match_estimated:
        estimated_zfw = int(float(match_estimated.group(1)))

    match_actual = re.search(pattern_actual, string)
    if match_actual:
        actual_zfw = int(float(match_actual.group(1)))

    return estimated_zfw, actual_zfw
