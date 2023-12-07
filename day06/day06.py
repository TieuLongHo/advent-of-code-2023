import os
import math


def part1(data: list) -> None:
    ranges = []
    result = 1
    for i, race in enumerate(data[0]):
        time = data[0][i]
        distance = data[1][i]
        found_start = False
        for j in range(time):
            if not found_start:
                if (time - j) * j > distance:
                    ranges.append([j, None])
                    found_start = True
            else:
                if (time - j) * j < distance:
                    ranges[i][1] = j - 1
                    break
    print(ranges)

    for points in ranges:
        result *= points[1] - points[0] + 1

    print(f"Part 1: {result}")


def math_part1(data: list) -> None:
    ranges = []
    result = 1
    for i, race in enumerate(data[0]):
        time = data[0][i]
        distance = data[1][i]
        d = (time**2) - (4 * distance)

        sol1 = (-time - math.sqrt(d)) / (-2)
        sol2 = (-time + math.sqrt(d)) / (-2)

        ranges.append([math.ceil(sol2), math.floor(sol1)])
    for points in ranges:
        result *= points[1] - points[0] + 1
    print(f"Part 1 with quadratic formula: {result}")


def part2(data: list) -> None:
    correct_data = []
    ranges = []
    for values in data:
        current_data = ""
        for num in values:
            current_data += str(num)
        correct_data.append(int(current_data))
    for i in range(correct_data[0]):
        if (correct_data[0] - i) * i > correct_data[1]:
            ranges.append(i)
            break
    for i in range(correct_data[0], -1, -1):
        if (correct_data[0] - i) * i > correct_data[1]:
            ranges.append(i)
            break
    result = ranges[1] - ranges[0] + 1
    print(f"Part 2: {result}")


if __name__ == "__main__":
    print("Advent of Code: Day 06")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input.txt")
    with open(file_path) as f:
        data = f.read().splitlines()
        races = []
        for d in data:
            d = list(map(int, d.split(":")[1].split()))
            races.append(d)

        part1(races)
        part2(races)
        math_part1(races)
