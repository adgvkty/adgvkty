import numpy as np
import matplotlib.pyplot as plt
import random
from typing import Dict, List, Set, Tuple
from collections import Counter
import statistics as st

#random.seed(41)

n = 20
k = 10000000


def new_class(n: int) -> List[int]:
    return [random.randint(1, 365) for _ in range(n)]


def new_class_dataset(n: int, k: int) -> List[List[int]]:
    return [new_class(n) for _ in range(k)]


def collision_probability(d: List[List[int]]) -> float:
    P = 0
    for lst in d:
        lst.sort()
        temp = []
        for i in range(len(lst)):
            if i != len(lst) - 1:
                if lst[i] == lst[i + 1]:
                    temp.append(lst[i])
        if temp:
            P += 1
    return P/k

d = new_class_dataset(n, k)
print(collision_probability(d))

