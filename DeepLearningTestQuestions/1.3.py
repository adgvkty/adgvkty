import numpy as np
import matplotlib.pyplot as plt
import random
from typing import Dict, List, Set, Tuple

input_dict = {'rozetka': ['iphone', 'macbook', 'ipad'],
              'fua': ['macbook', 'ipad'],
              'citrus': ['iphone', 'macbook', 'earpods'],
              'allo': ['earpods', 'iphone']}


def dict_inv(i_d: Dict) -> Dict:  # для быстроты input_dict -> i_d
    items = list(input_dict.values())
    items = set([item for t in items for item in t])  # list-of-tuple в просто list; благодаря set без повторений
    items = list(items)  # превращаем множество в список
    keys = list(input_dict.keys())  # и получаем список ключей из словаря-аргумента
    r_d = {}  # создаем массив для возврата
    for i in range(len(items)):  # для каждого товара
        temp = []  # создаем свой темп
        for x in range(len(keys)):  # просматриваем каждый ключ(магазин) и его значения
            if items[i] in input_dict.get(keys[x]):  # если товар есть среди значений х-вого ключа(магазина)
                temp.append(keys[x])  # добавляем ключ(название магазина) в временный список
        r_d.update({items[i]: set(temp)})  # добавляем в словарь пару i-ый предмет:все магазины из списка
    return r_d






    """
    items = list(i_d.values())
    items = set([item for t in items for item in t]) # list-of-tuple в просто list; благодаря set без повторений
    items = list(items)
    r_d = {}
    for item in items:
        r_d.setdefault(item, [])
    i_keys = list(i_d.keys())
    r_keys = list(r_d.keys())
    for key in i_keys:
        temp = i_d.get(key)  # значения ключа
        for x in range(len(temp)):
            for i in range(len(r_keys)):
                if temp[x] == r_keys[i]:
                    r_d[r_keys[i]].append[key]
    print(r_d)
    """



output_dict = dict_inv(input_dict)
print(output_dict)