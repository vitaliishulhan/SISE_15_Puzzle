from enum import Enum


class Operation(Enum):
    L = (-1, 0)
    R = (1, 0)
    U = (0, -1)
    D = (0, 1)
