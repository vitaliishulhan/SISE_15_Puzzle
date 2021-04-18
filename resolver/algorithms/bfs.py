from typing import Optional

from model.state import State
from model.operation import Operation
from algorithms.getpath import get_path


def bfs(w: int, h: int, initial_state: tuple, goal_state: tuple,
        operations_order: tuple[Operation, Operation, Operation, Operation]) -> tuple[str, int, int, int]:
    if initial_state == goal_state:
        return "", 0, 0, 0

    explored: set[State, ...] = set()
    front_set: set[State, ...] = set()

    State.w = w
    State.h = h
    State.goal_state = goal_state
    State.operations_order = operations_order

    init = State(initial_state)
    front_set.add(init)

    max_depth = 0

    def recursive_search(state_list: list[State, ...]) -> tuple[Optional[State], int]:
        if len(state_list) == 0:
            return None

        nonlocal max_depth
        if max_depth < state_list[0].path_price:
            max_depth = state_list[0].path_price

        all_neighbours: list[State, ...] = list()

        for state in state_list:
            front_set.remove(state)
            explored.add(state)

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
                    max_depth = neighbour.path_price
                    return neighbour

            all_neighbours.extend(neighbours)

        return recursive_search(all_neighbours)

    res = recursive_search([init])

    return get_path(res), max_depth, len(front_set) + len(explored), len(explored)
