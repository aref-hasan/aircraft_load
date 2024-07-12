import re
from typing import Optional, Tuple

def StorePaxDataAction(string: str) -> Tuple[Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[str]]:
    """
    Parses the input string to extract the passenger information including total passengers,
    passengers in economy class, business class, jump seats, standby, male, female, children,
    infants, total bags, total bag weight, and baggage weight type.

    Args:
        string (str): The input string containing the passenger information.

    Returns:
        Tuple[Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[float], Optional[str]]:
            - total_pax: Total number of passengers.
            - economy_class: Number of passengers in economy class.
            - business_class: Number of passengers in business class.
            - jump_seat: Number of passengers in jump seats.
            - standby: Number of standby passengers.
            - male: Number of male passengers.
            - female: Number of female passengers.
            - child: Number of child passengers.
            - infant: Number of infant passengers.
            - total_bag: Total number of bags.
            - total_bag_weight: Total weight of bags in kilograms.
            - baggage_weight_type: Type of baggage weight calculation.
    """
    total_pax = None
    economy_class = None
    business_class = None
    jump_seat = None
    standby = None
    male = None
    female = None
    child = None
    infant = None
    total_bag = None
    total_bag_weight = None
    baggage_weight_type = None
    
    if string is not None:
        # Extracting total passengers
        pattern_total_pax = r"TOTAL Pax: (\d+)"
        match_total_pax = re.search(pattern_total_pax, string)
        if match_total_pax:
            total_pax = int(match_total_pax.group(1))
        
        # Extracting economy class passengers
        pattern_economy_class = r"Y: (\d+)"
        match_economy_class = re.search(pattern_economy_class, string)
        if match_economy_class:
            economy_class = int(match_economy_class.group(1))

        # Extracting business class passengers
        pattern_business_class = r"J: (\d+)"
        match_business_class = re.search(pattern_business_class, string)
        if match_business_class:
            business_class = int(match_business_class.group(1))

        # Extracting jump seat passengers
        pattern_jump_seat = r"Jump: (\d+)"
        match_jump_seat = re.search(pattern_jump_seat, string)
        if match_jump_seat:
            jump_seat = int(match_jump_seat.group(1))

        # Extracting standby passengers
        pattern_standby = r"StandBy: (\w+)"
        match_standby = re.search(pattern_standby, string)
        if match_standby:
            standby = None if match_standby.group(1) == "NULL" else int(match_standby.group(1))

        # Extracting male passengers
        pattern_male = r"Male: (\d+)"
        match_male = re.search(pattern_male, string)
        if match_male:
            male = int(match_male.group(1))

        # Extracting female passengers
        pattern_female = r"Female: (\d+)"
        match_female = re.search(pattern_female, string)
        if match_female:
            female = int(match_female.group(1))

        # Extracting child passengers
        pattern_child = r"Child: (\d+)"
        match_child = re.search(pattern_child, string)
        if match_child:
            child = int(match_child.group(1))

        # Extracting infant passengers
        pattern_infant = r"Infant: (\d+)"
        match_infant = re.search(pattern_infant, string)
        if match_infant:
            infant = int(match_infant.group(1))

        # Extracting total bags
        pattern_total_bag = r"Total bag: (\d+)"
        match_total_bag = re.search(pattern_total_bag, string)
        if match_total_bag:
            total_bag = int(match_total_bag.group(1))

        # Extracting total bag weight
        pattern_total_bag_weight = r"Total bag weight: ([\d.]+) KG"
        match_total_bag_weight = re.search(pattern_total_bag_weight, string)
        if match_total_bag_weight:
            total_bag_weight = int(float(match_total_bag_weight.group(1)))

        # Extracting baggage weight type
        pattern_baggage_weight_type = r"Baggage weight type: (\w+)"
        match_baggage_weight_type = re.search(pattern_baggage_weight_type, string)
        if match_baggage_weight_type:
            baggage_weight_type = match_baggage_weight_type.group(1)
    
    return total_pax, economy_class, business_class, jump_seat, standby, male, female, child, infant, total_bag, total_bag_weight, baggage_weight_type