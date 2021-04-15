from model.state import State
from typing import Union


def get_path(state: State) -> Union[str, int]:
    if state is None:
        return -1

    def get_path_reversed(s: State) -> str:
        if s.parent is None:
            return ""

        res: str = s.operation.name + get_path_reversed(s.parent)
        return res

    return get_path_reversed(state)[::-1]
