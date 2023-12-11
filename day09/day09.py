import os


def part1(data: list) -> None:
    print(f"Part 1: {arrange_data(data, True)}")


def part2(data: list) -> None:
    print(f"Part 2: {arrange_data(data, False)}")


def calc(pyramid: list, part1: bool) -> None:
    for row in pyramid:
        if pyramid.index(row) == 0:
            row.append(0)
            continue
        if part1:
            row.append(pyramid[pyramid.index(row) - 1][-1] + row[-1])
            continue
        row.insert(0, row[0] - pyramid[pyramid.index(row) - 1][0])


def arrange_data(data: list, part1: bool) -> list:
    pyramid = []
    result = 0

    for d in data:
        pyramid = [d]
        for row in pyramid:
            pyrow = []
            for i, num in enumerate(row):
                if i == 0:
                    continue
                pyrow.append(num - row[i - 1])
            pyramid.append(pyrow)
            if sum(pyrow) == 0:
                break
        pyramid.reverse()
        calc(pyramid, part1)
        if part1:
            result += pyramid[-1][-1]
        else:
            result += pyramid[-1][0]
    return result


if __name__ == "__main__":
    print("Advent of Code: Day 09")
    extracted_data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input.txt")
    with open(file_path) as f:
        data = f.read().splitlines()
        for d in data:
            extracted_data.append([int(x) for x in d.split()])
        part1(extracted_data)
        part2(extracted_data)
