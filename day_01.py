def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    return [int(line.replace("\n", "")) for line in lines]


def solver_1(lines):
    counter = 0
    for i in range(1, len(lines)):
        A = lines[i-1]
        B = lines[i]
        if B > A:
            counter += 1
    return counter


def solver_2(lines):
    counter = 0
    for i in range(3, len(lines)):
        A = sum(lines[i-3:i])
        B = sum(lines[i-2:i+1])
        if B > A:
            counter += 1
    return counter


if __name__ == '__main__':
    filename = '01.txt'

    lines = parser(loader(filename))

    sol1 = solver_1(lines)
    sol2 = solver_2(lines)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
