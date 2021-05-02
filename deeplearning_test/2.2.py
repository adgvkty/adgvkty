import numpy as np
import matplotlib.pyplot as plt
import random
from typing import Dict, List, Set, Tuple
from collections import Counter

random.seed(41)

a = [random.randint(1, 365) for i in range(25)]


mylist = [20, 30, 25, 20]

def happy_b_day(a: List[int]) -> List[int]:
    a.sort()  # сортируем список
    temp = []
    for i in range(len(a)):  # перебираем список
        if i != len(a)-1:  # проверка чтобы не вылететь из массива (ибо элементов 25, но индекс последнего - 24)
            if a[i] == a[i+1]:  # если предыдущий элемент равен следующему, то
                temp.append(a[i])  # закидываем во временный список
    a = temp  # ну и делаем временного списка основной
    return a

def happy_b_day_easy(a: List[int]) -> List[int]:
    res = [i for i, v in Counter(a).items() if v > 1]  # немного очень сложных манипуляций с синтаксисом питона
    return res

print(happy_b_day_easy(a))
print(happy_b_day(a))