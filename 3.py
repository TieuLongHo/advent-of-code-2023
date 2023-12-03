import re

sum = 0
symbols = {}


def repair():
    with open("3.txt", "r") as file:
        lines = file.read().splitlines()

        for i, line in enumerate(lines):
            isdigit = False
            for j, char in enumerate(line):
                if char.isdigit():
                    if not isdigit:
                        isdigit = True
                        adding(has_around(lines, i, j))
                else:
                    isdigit = False


def has_around(lines: list, index: int, char_index: int) -> int:
    end = -1
    count = 0
    found_end = False
    while (char_index + count) < len(lines[index]):
        if not lines[index][char_index + count].isdigit():
            found_end = True
            end = count
            break
        count += 1
    if not found_end:
        end = count

    start_point = char_index - 1 if char_index > 0 else 0
    end_point = char_index + end + 1

    range = [start_point, end_point]

    pattern = "[\d.]"

    # check above
    if index != 0:
        s = re.sub(pattern, "", lines[index - 1][range[0] : range[1]])
        if s != "":
            return int(lines[index][char_index : char_index + end])

    # check current
    if re.sub(pattern, "", lines[index][range[0] : range[1]]) != "":
        return int(lines[index][char_index : char_index + end])

    # check below
    if index + 1 != len(lines):
        if re.sub(pattern, "", lines[index + 1][range[0] : range[1]]) != "":
            return int(lines[index][char_index : char_index + end])
    return 0


def adding(number: int) -> None:
    global sum
    sum += number


def gear():
    with open("3.txt", "r") as file:
        lines = file.read().splitlines()
        stars = []

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == "*":
                    stars.append((i, j))
        for star in stars:
            check_around(star, lines)


def check_around(pos: tuple, lines: list):
    ratio = []
    if pos[0] != 0:
        for i in range(-1, 2):
            start, end = find_endpoints(lines[pos[0] - 1], pos[1] + i)
            if start is not None:
                if int(re.sub("\D", "", lines[pos[0] - 1][start:end])) not in ratio:
                    ratio.append(int(re.sub("\D", "", lines[pos[0] - 1][start:end])))

    for i in range(-1, 2, 2):
        start, end = find_endpoints(lines[pos[0]], pos[1] + i)
        if start is not None:
            ratio.append(int(re.sub("\D", "", lines[pos[0]][start:end])))
    if pos[0] + 1 != len(lines):
        for i in range(-1, 2):
            start, end = find_endpoints(lines[pos[0] + 1], pos[1] + i)
            if start is not None:
                if int(re.sub("\D", "", lines[pos[0] + 1][start:end])) not in ratio:
                    ratio.append(int(re.sub("\D", "", lines[pos[0] + 1][start:end])))
    if len(ratio) == 2:
        adding(ratio[0] * ratio[1])


def find_endpoints(string: str, pos: int) -> tuple:
    count = 0
    start_found = False
    start = 0
    end_found = False
    end = 0
    while not start_found:
        if pos != 0:
            if pos - count > 0:
                if string[pos - count].isdigit():
                    count += 1
                else:
                    start_found = True
                    if count > 0:
                        start = pos - count + 1
                    else:
                        start = None
            else:
                start = 0
                start_found = True
        else:
            start = 0
            start_found = True
    count = 0

    while not end_found:
        if pos != len(string):
            if pos + count + 1 <= len(string):
                if string[pos + count].isdigit():
                    count += 1
                else:
                    if count > 0:
                        end = pos + count + 1
                    else:
                        end = None
                    end_found = True
            else:
                end = len(string)
                end_found = True

        else:
            end = len(string)
            end_found = True
    return (start, end)


repair()
print(f"Part 1: {sum}")
sum = 0
gear()
print(f"Part 2: {sum}")
