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

def price_statistics(spd: Dict) -> Dict:
    values = spd.values()
    values = list(values)
    values.sort()
    spd.clear()
    spd.update({'min': min(values)})
    spd.update({'max': max(values)})
    spd.update({'mean': int(sum(values) / len(values))})
    n = len(values)
    index = n // 2
    if n % 2:
        value = values[index]
        print('suka')
    else:
        value = sum(values[index - 1:index + 1]) / 2
    spd.update({'median': value})
    return spd




price_stat = price_statistics(shop_price_dict)
print(price_stat)
