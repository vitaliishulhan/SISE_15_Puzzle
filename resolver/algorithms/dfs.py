from typing import Optional

from model.state import State
from model.operation import Operation
from algorithms.getpath import get_path


def dfs(w: int, h: int, initial_state: tuple, goal_state: tuple,
        operations_order: tuple[Operation, Operation, Operation, Operation]) -> tuple[str, int, int, int]:
    if initial_state == goal_state:
        return "", 0, 0, 0

    front_set: set = set()
    explored: set = set()

    State.w = w
    State.h = h
    State.goal_state = goal_state
    State.operations_order = operations_order

    init = State(initial_state)
    front_set.add(init)

    max_depth: int = 0

    def recursive_search(state: State) -> Optional[State]:
        nonlocal max_depth

        if max_depth < state.path_price:
            max_depth = state.path_price

        if state.path_price == 20:
            if state.test():
                return state, 20
            else:
                ns = state.get_neighbours()
                for n in ns:
                    if n.test():
                        max_depth = 21
                        return n
                return None

        explored.add(state)

        neighbours: tuple[State, ...] = tuple(
            filter(
                lambda s: s not in explored,
                state.get_neighbours()
            )
        )

        for neighbour in neighbours:
            front_set.add(neighbour)

        for neighbour in neighbours:
            if neighbour.test():
                return neighbour

        for neighbour in neighbours:
            some_state = recursive_search(neighbour)
            if some_state is not None:
                return some_state

        return None

    res = recursive_search(init)

    return get_path(res), max_depth, len(front_set), len(explored)






