import numpy as np


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    lines = [list(map(int, line.replace("\n", ""))) for line in lines]
    return np.asarray(lines)


def solver_1(lines):
    means = np.mean(lines, axis=0)

    gamma = np.where(means < 0.5, 0, 1)
    gamma = list(map(str, gamma))
    gamma = int("".join(gamma), 2)

    epsilon = np.where(means < 0.5, 1, 0)
    epsilon = list(map(str, epsilon))
    epsilon = int("".join(epsilon), 2)

    return gamma*epsilon


def solver_2(lines):
    means = np.mean(lines, axis=0)
    gamma = np.where(means < 0.5, 0, 1)
    epsilon = np.where(means < 0.5, 1, 0)

    oxygen_gen = lines.copy()
    co2_scrubber = lines.copy()

    for i in range(len(lines[0])):
        if len(oxygen_gen) > 1:
            keeper = 1 if np.mean(oxygen_gen, axis=0)[i] >= 0.5 else 0
            oxygen_gen = list(filter(lambda x: x[i] == keeper, oxygen_gen))
        if len(co2_scrubber) > 1:
            keeper = 1 if np.mean(co2_scrubber, axis=0)[i] < 0.5 else 0
            co2_scrubber = list(filter(lambda x: x[i] == keeper, co2_scrubber))

    oxygen_gen = list(map(str, oxygen_gen[0]))
    oxygen_gen = int("".join(oxygen_gen), 2)

    co2_scrubber = list(map(str, co2_scrubber[0]))
    co2_scrubber = int("".join(co2_scrubber), 2)

    return oxygen_gen*co2_scrubber


if __name__ == '__main__':
    filename = '03.txt'

    lines = parser(loader(filename))

    sol1 = solver_1(lines)
    sol2 = solver_2(lines)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
