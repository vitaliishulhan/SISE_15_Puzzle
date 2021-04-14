import sys

from state import State
from operation import Operation
from getpath import get_path


def dfs(w: int, h: int, initial_state: tuple, goal_state: tuple,
        operations_order: tuple[Operation, Operation, Operation, Operation]) -> str:
    if initial_state == goal_state:
        return ""

    front_tier: list = list()
    explored: set = set()

    State.w = w
    State.h = h
    State.goal_state = goal_state
    State.operations_order = operations_order

    init = State(initial_state)
    front_tier.append(init)

    def recursive_search(state: State, depth: int = 0):
        explored.add(state)
        if depth == 20:
            if state.test():
                print("max depth")
                return state
            else:
                return None

        neighbours: tuple[State, ...] = tuple(
            filter(
                lambda s: s not in explored,
                state.get_neighbours()
            )
        )

        for neighbour in neighbours:
            front_tier.append(neighbour)
            if neighbour.test():
                return neighbour
            else:
                some_state = recursive_search(neighbour, depth + 1)
                if some_state is not None:
                    return some_state

    return get_path(recursive_search(init))






