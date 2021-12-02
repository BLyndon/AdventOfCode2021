class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0

    def distance(self):
        return abs(self.x)*abs(self.y)

    def move(self, dir, value):
        if dir == 'up':
            self.x -= value
        elif dir == 'down':
            self.x += value
        elif dir == 'forward':
            self.y += value

    def navigate(self, instruction):
        action, value = instruction
        self.move(action, value)


class Submarine_Pt2(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def move(self, dir, value):
        if dir == 'up':
            self.aim -= value
        elif dir == 'down':
            self.aim += value
        elif dir == 'forward':
            self.y += self.aim*value
            self.x += value


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    lines = [line.replace("\n", "") for line in lines]
    instructions = [(line.split(" ")[0], int(line.split(" ")[1]))
                    for line in lines]
    return instructions


def solver_1(instructions):
    ship = Submarine()
    for instruction in instructions:
        ship.navigate(instruction)
    return ship.distance()


def solver_2(instructions):
    ship = Submarine_Pt2()
    for instruction in instructions:
        ship.navigate(instruction)
    return ship.distance()


if __name__ == '__main__':
    filename = '02.txt'

    instructions = parser(loader(filename))

    sol1 = solver_1(instructions)
    sol2 = solver_2(instructions)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
