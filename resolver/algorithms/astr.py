from typing import Callable, Optional

from model.operation import Operation
from model.state import State
from algorithms.getpath import get_path


def a_star(w: int, h: int,
           initial_state: tuple, goal_state: tuple,
           operations_order: tuple[Operation, Operation, Operation, Operation],
           get_distance: Callable[[State], int]):
    State.w = w
    State.h = h
    State.goal_state = goal_state
    State.operations_order = operations_order

    explored: set = set()

    def recursive_search(state_list: list[State]) -> Optional[State]:
        if len(state_list) == 0:
            return None

        state = state_list[0]

        state_list.remove(state)
        explored.add(state)

        if state.test():
            return state

        neighbours: tuple[State, ...] = tuple(
            filter(
                lambda s: s not in explored,
                state.get_neighbours()
            )
        )

        state_list.extend(neighbours)
        state_list.sort(key=lambda s: s.path_price + get_distance(s))

        return recursive_search(state_list)

    return get_path(recursive_search([State(initial_state)]))
