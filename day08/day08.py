import os
from math import gcd


def part1(data: list) -> None:
    arrived = False
    repetitions = 0
    current_pos = "AAA"
    while not arrived:
        for dir in data[0]:
            repetitions += 1
            match dir:
                case "R":
                    current_pos = data[1][current_pos][1]
                    if current_pos == "ZZZ":
                        arrived = True
                        break
                case "L":
                    current_pos = data[1][current_pos][0]
                    if current_pos == "ZZZ":
                        arrived = True
                        break
    print(f"Part 1: {repetitions}")


def part2(data: list) -> None:
    steps = {}
    arrived = False
    repetitions = 0
    current_pos = data[2]
    while not arrived:
        for dir in data[0]:
            repetitions += 1
            new_pos = []
            for start in current_pos:
                match dir:
                    case "R":
                        new_pos.append(data[1][start][1])
                    case "L":
                        new_pos.append(data[1][start][0])

            current_pos = new_pos
            for i, pos in enumerate(current_pos):
                if pos.endswith("Z"):
                    if steps.get(i) is None:
                        steps[i] = [repetitions, 1]
                    else:
                        inni = steps.get(i)[0] * steps.get(i)[1]
                        steps[i] = [repetitions - inni, steps[i][1] + 1]
        if len(steps) == len(current_pos):
            break

    lcm = 1
    for num in steps:
        lcm = lcm * steps[num][0] // gcd(lcm, steps[num][0])

    print(f"Part 2: {lcm}")


if __name__ == "__main__":
    direction = ""
    routes = {}
    print("Advent of Code: Day 08")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input.txt")
    with open(file_path) as f:
        data = f.read().splitlines()
        start = []
        for i, d in enumerate(data):
            if i == 0:
                direction = d
                continue
            if i == 1:
                continue
            d = d.split("=")

            d2 = (
                d[1]
                .strip()
                .replace("(", "")
                .replace(")", "")
                .replace(" ", "")
                .split(",")
            )
            routes[d[0].strip()] = d2
            if d[0].strip().endswith("A"):
                start.append(d[0].strip())

        part1([direction, routes])
        part2([direction, routes, start])
