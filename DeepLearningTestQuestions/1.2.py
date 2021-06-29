import numpy as np
import matplotlib.pyplot as plt
import random
from typing import Dict, List, Set, Tuple
import statistics as st

shop_price_dict = {'citrus': 47999,
                   'newtime': 37530,
                   'buyua': 39032,
                   'storeinua': 37572,
                   'allo': 48499,
                   'istore': 39999,
                   'tehnokrat': 39340,
                   'estore': 40169,
                   'gstore': 40792,
                   'touch': 39330,
                   'bigmag': 37900, }


# -> Dict

def filter_shops_by_price(spd: Dict, p_min: float, p_max: float) -> Set[str]:
    set_str = set()
    for i in range(len(spd)):
        values = list(spd.popitem())
        if p_min <= values[1] <= p_max:
            set_str.add(values[0])
    return set_str


list_of_filtered_shops = filter_shops_by_price(shop_price_dict, 39000, 40000)
print(list_of_filtered_shops)