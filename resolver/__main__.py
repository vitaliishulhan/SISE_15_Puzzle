import glob

from model.operation import Operation
from algorithms.astr import a_star
from algorithms.metrics import *


def read_tables(dirpath: str) -> list:
    files = glob.glob(f'{dirpath}/*.txt')

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for file in files:
        print(file)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    res = []

    for f in files:
        with open(f, 'r') as file:
            w, h = map(lambda item: int(item), file.readline().split(' '))

            puzzle = []
            for line in file.readlines():
                for num in tuple(map(lambda item: int(item), line.split(' '))):
                    puzzle.append(num)

            res.append((w, h, tuple(puzzle)))

    return res


if __name__ == "__main__":
    tables = read_tables("../tables")

    orders = [
        (Operation.R, Operation.D, Operation.U, Operation.L),
        (Operation.R, Operation.D, Operation.L, Operation.U),
        (Operation.D, Operation.R, Operation.U, Operation.L),
        (Operation.D, Operation.R, Operation.L, Operation.U),
        (Operation.L, Operation.U, Operation.D, Operation.R),
        (Operation.L, Operation.U, Operation.R, Operation.D),
        (Operation.U, Operation.L, Operation.D, Operation.R),
        (Operation.U, Operation.L, Operation.R, Operation.D)
    ]

    # for order in orders:
    print("ORDER:", *tuple(map(lambda o: o.name, orders[0])))
    for table in tables:
        print(table)
        result = a_star(table[0], table[1],  # dimension
                        table[2],  # init state
                        tuple([i for i in range(1, table[0] * table[1])] + [0]),  # final state
                        orders[0],  # operations_order
                        get_manhattan_distance)
        print(result)
        # break
