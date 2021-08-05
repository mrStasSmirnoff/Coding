""""
Lesson 1 - Iterations
"""

# Binary Gap Problem

import logging as log


def iteration_solution_1(n:int) -> str:
    """
    :param n: Interger as an intut
    :return: longest binary gap
    """

    int_to_str = str(bin(n))[2:]
    counter = 0

    for i in range(len(int_to_str)):
        if int_to_str[i] == '0':
            counter += 1

    return int_to_str


N = '29210'
value = iteration_solution_1(N)
print(f"printed binary value: {value}")

if __name__ == "__main__":
    log.info("Binary Gap problem solution")