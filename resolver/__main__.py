import sys
import time

from model.operation import Operation
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astr import a_star
from algorithms.metrics import *


def read_table(filepath: str) -> tuple[int, int, tuple[int, ...]]:
    with open(filepath, 'r') as f:
        w, h = map(lambda item: int(item), f.readline().split(' '))

        puzzle = []
        for line in f.readlines():
            for num in tuple(map(lambda item: int(item), line.split(' '))):
                puzzle.append(num)

    return w, h, tuple(puzzle)


if __name__ == "__main__":
    start_time = time.time()

    if len(sys.argv) != 6:
        print("Program takes 5 arguments:\n"
              "\t1) algorithm name acronym (bfs, dfs, astr)\n"
              "\t2) operations acronyms list (R (right),D (down),U (up),L (left)) in desired order\n"
              "\tOR\n"
              "\t2) metric acronym (hamm, manh) if selected algorithm is astr\n"
              "\t3) path to the file with puzzle\n"
              "\t4) path to the file, where solution will be saved\n"
              "\t5) path to the file, where statistics will be saved\n")
        sys.exit(1)

    algorithm_name: str = sys.argv[1]
    if algorithm_name not in ('bfs', 'dfs', 'astr'):
        print('Fatal: algorithm name can be bfs, dfs or astr')
        sys.exit(1)

    if algorithm_name in ('bfs', 'dfs'):
        operations_order: str = ""

        if len(sys.argv[2]) != 4:
            print('Fatal: operations order list must contain 4 elements')
            sys.exit(1)

        for op in sys.argv[2]:
            if op in operations_order or op not in ('R', 'D', 'U', 'L'):
                print('Fatal: operations order must contain R,D,U, and L without duplicates')
                sys.exit(1)
            operations_order += op

        sec_arg = Operation.get_order(operations_order)
    else:
        metric_name = sys.argv[2]
        if metric_name not in ('hamm', 'manh'):
            print('Fatal: metric_name must be hamm or manh')
            sys.exit(1)

        sec_arg = get_hamming_distance if metric_name == 'hamm' else get_manhattan_distance

    try:
        table = read_table(sys.argv[3])
    except FileNotFoundError:
        print(f"Fatal: No such file: '{sys.argv[3]}'")
        sys.exit(1)

    chosen_algorithm = {
        'bfs': bfs,
        'dfs': dfs,
        'astr': a_star
    }[algorithm_name]

    result = chosen_algorithm(table[0], table[1],
                              table[2],
                              tuple([i for i in range(1, table[0] * table[1])] + [0]),
                              sec_arg)

    with open(sys.argv[4], 'w') as file:
        if result[0] != -1:
            file.write(str(len(result[0])) + "\n" + result[0])
        else:
            file.write("-1")

    with open(sys.argv[5], 'w') as file:
        file.write(("-1" if result[0] == -1 else str(len(result[0]))) + "\n" +
                   str(result[2]) + "\n" +
                   str(result[3]) + "\n" +
                   str(result[1]) + "\n" +
                   str(round((time.time() - start_time)*1000000) / 1000))
