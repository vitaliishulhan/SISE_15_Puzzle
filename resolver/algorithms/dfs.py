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
    front_set.add((init, 0))

    # max_depth: int = 0

    def recursive_search(state: tuple[State, int]) -> Optional[State]:
        # nonlocal max_depth

        # if max_depth < state[1]:
        #     max_depth = state.path_price

        if state[1] == 20:
            if state[0].test():
                return state[0], 20
            else:
                return None, 20

        explored.add(state)

        neighbours: tuple[State, ...] = tuple(
            filter(
                lambda s: s not in explored,
                map(lambda item: (item, state[1] + 1), state[0].get_neighbours())
            )
        )

        for neighbour in neighbours:
            front_set.add(neighbour)

        for neighbour in neighbours:
            if neighbour[0].test():
                return neighbour

        for neighbour in neighbours:
            some_state = recursive_search(neighbour)
            if some_state[0] is not None:
                return some_state

        return None, state[1]

    res = recursive_search((init, 0))

    return get_path(res[0]), max(map(lambda item: item[1], front_set)), len(front_set), len(explored)
