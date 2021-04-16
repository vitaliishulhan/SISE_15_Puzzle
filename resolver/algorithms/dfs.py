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
    front_set.add(init)

    global_depth: int = 0

    def recursive_search(state: State, depth: int = 0) -> tuple[Optional[State], int]:
        nonlocal global_depth
        if depth > global_depth:
            global_depth = depth
        front_set.remove(state)
        explored.add(state)

        if depth == 20:
            if state.test():
                return state, 20
            else:
                return None, 20

        neighbours: tuple[State, ...] = tuple(
            filter(
                lambda s: s not in explored and s not in front_set,
                state.get_neighbours()
            )
        )

        for neighbour in neighbours:
            front_set.add(neighbour)

        for neighbour in neighbours:
            if neighbour.test():
                return neighbour, depth + 1
            else:
                some_state, returned_depth = recursive_search(neighbour, depth + 1)
                if some_state is not None:
                    return some_state, returned_depth

        return None, depth

    res = recursive_search(init)

    return get_path(res[0]), max(res[1], global_depth), len(front_set) + len(explored), len(explored)






