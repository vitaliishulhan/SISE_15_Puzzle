from typing import Callable, Optional

from model.operation import Operation
from model.state import State
from algorithms.getpath import get_path


def a_star(w: int, h: int,
           initial_state: tuple, goal_state: tuple,
           get_distance: Callable[[State], int]):
    State.w = w
    State.h = h
    State.goal_state = goal_state
    State.operations_order = Operation.get_order('URDL')

    front_set: set = set()
    explored: set = set()

    init = State(initial_state)
    front_set.add((init, 0))

    def recursive_search(state_list: list[tuple[State, int], ...]) -> tuple[Optional[State], int]:
        if len(state_list) == 0:
            all_states_depth = [e[1] for e in front_set]
            all_states_depth.extend([e[1] for e in explored])
            return None, max(all_states_depth)

        state = state_list[0]

        front_set.remove(state)
        state_list.remove(state)
        explored.add(state)

        if state[0].test():
            return state

        neighbours: tuple[tuple[State, int], ...] = tuple(
            map(
                lambda s: (s, state[1] + 1),
                tuple(
                    filter(
                        lambda s: s not in explored,
                        state[0].get_neighbours()
                    )
                )
            )
        )

        for neighbour in neighbours:
            front_set.add(neighbour)

        state_list.extend(neighbours)
        state_list.sort(key=lambda s: s[0].path_price + get_distance(s[0]))

        return recursive_search(state_list)

    res = recursive_search([(init, 0)])

    return get_path(res[0]), res[1], len(front_set) + len(explored), len(explored)
