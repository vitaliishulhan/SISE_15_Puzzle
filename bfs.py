from state import State
from operation import Operation
from getpath import get_path


def bfs(w: int, h: int, initial_state: tuple, goal_state: tuple,
        operations_order: tuple[Operation, Operation, Operation, Operation]) -> str:

    if initial_state == goal_state:
        return ""


    explored: set = set()

    State.w = w
    State.h = h
    State.goal_state = goal_state
    State.operations_order = operations_order

    def recursive_search(state_list):
        if len(state_list) == 0:
            return None

        for state in state_list:
            explored.add(state)
            if state.test():
                return state

        neighbours = list()
        for state in state_list:
            neighbours.extend(
                filter(
                    lambda s: s not in explored,
                    state.get_neighbours()
                )
            )
        return recursive_search(neighbours)

    return get_path(recursive_search([State(initial_state)]))