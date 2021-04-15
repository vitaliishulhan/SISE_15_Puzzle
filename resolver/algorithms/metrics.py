from model.state import State


def get_hamming_distance(s: State) -> int:
    goal_state: tuple = State.goal_state
    h: int = State.h
    w: int = State.w

    distance: int = 0

    for y in range(h):
        for x in range(w):
            if s.table[y*w + x] != 0 and s.table[y*w + x] != goal_state[y*w + x]:
                distance += 1

    return distance


def get_manhattan_distance(s: State) -> int:
    try:
        coord_goal_state = State.coord_goal_state
    except AttributeError:
        coord_goal_state = State.coord_goal_state = get_coord_state_table(State.goal_state)

    coord_state = get_coord_state_table(s.table)

    distance: int = 0

    for i in range(len(coord_state)):
        e1 = coord_state[i]
        e2 = coord_goal_state[i]
        distance += abs(e1[0] - e2[0]) + abs(e1[1] - e2[1])

    return distance


def get_coord_state_table(table: tuple) -> tuple[tuple[int, int], ...]:
    res = [None for i in range(State.w * State.h)]

    for y in range(State.h):
        for x in range(State.w):
            res[table[y*State.w + x]]: tuple[int, int] = x, y

    res.remove(res[0])

    return tuple(res)
