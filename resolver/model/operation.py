from __future__ import annotations
from enum import Enum


class Operation(Enum):
    L = (-1, 0)
    R = (1, 0)
    U = (0, -1)
    D = (0, 1)

    @classmethod
    def get_order(cls, order: str) -> tuple[Operation, ...]:
        res = []
        for op in order:
            res.append(Operation[op])
        return tuple(res)
