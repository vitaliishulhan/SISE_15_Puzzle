from __future__ import annotations
from operation import Operation
from numpy import array


class State:
    w: int = 0,
    h: int = 0,
    operations_order: tuple[Operation, Operation, Operation, Operation] = None
    goal_state: tuple = None

    def __init__(self,
                 table: tuple,
                 parent: State = None,
                 operation: Operation = None,
                 path_price: int = 0):

        self._table = table
        self._parent = parent
        self._operation = operation
        self._path_price = path_price

        for i in range(self.h):
            for j in range(self.w):
                if table[self.w * i + j] == 0:
                    self._p0 = j, i
                    break

    @property
    def table(self):
        return self._table

    @property
    def parent(self):
        return self._parent

    @property
    def operation(self):
        return self._operation

    @property
    def path_price(self):
        return self._path_price

    # take from dict [1,0], [-1,0], [0,1] or [0,-1] according to operator
    # and get coordinates of element to swap
    # if one of two coordinates is less than 0,
    # return the same table
    def make_operation(self, operation: Operation) -> State:
        new_p0 = array(self._p0) + array(operation.value)

        if new_p0[0] == -1 or new_p0[0] == self.w or new_p0[1] == -1 or new_p0[1] == self.h:
            return self

        new_table = list(self._table)

        new_table[self._p0[1] * self.w + self._p0[0]], \
        new_table[new_p0[1] * self.w + new_p0[0]] = new_table[new_p0[1] * self.w + new_p0[0]], \
                                                    new_table[self._p0[1] * self.w + self._p0[0]]

        return State(tuple(new_table), self, operation, self._path_price + 1)

    def get_neighbours(self) -> tuple:
        if self.operations_order is None:
            raise ValueError("Operator order must be assigned before")

        return tuple(filter(lambda state: state is not self, [self.make_operation(operation) for operation in self.operations_order]))

    def __eq__(self, other: State) -> bool:
        return self._table == other._table

    def __hash__(self):
        return hash(self._table)

    def test(self) -> bool:
        return self._table == self.goal_state

    def __str__(self):
        res = ""
        res += "~~~~~~~\n"
        for y in range(State.h):
            res += str(self._table[y * State.w:(y + 1) * State.w]) + "\n"
        res += "Initial state: " + ("Yes" if self.parent is None else "No") + "\n"
        res += "position of 0: " + str(self._p0) + "\n"
        res += "operation: " + (self.operation.name if self.operation is not None else "NONE") + "\n"
        res += "path price: " + str(self.path_price) + "\n"
        res += "~~~~~~~"
        return res
