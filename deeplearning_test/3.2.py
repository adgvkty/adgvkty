import numpy as np
import matplotlib.pyplot as plt
import random
from typing import Dict, List, Set, Tuple

V = [-0.7, 3.5]
origin = [0], [0]

plt.quiver(*origin, V[0], V[1], color=['r'], scale=10)
plt.show()