import re


def part1():
    sum = 0
    with open("1.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            digits = re.sub(r"\D", "", line)
            number = digits[0] + digits[-1]
            sum += int(number)
        print("Part 1: " + str(sum))


def part2():
    sum = 0
    digits_string = {
        "one": "o1e",
        "two": "tw2o",
        "three": "t3hree",
        "four": "f4our",
        "five": "f5ive",
        "six": "s6ix",
        "seven": "s7even",
        "eight": "e8ight",
        "nine": "n9ine",
        "zero": "z0ero",
    }

    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    file = open("1.txt", "r")
    lines = file.readlines()
    for line in lines:
        for key, value in digits_string.items():
            line = line.replace(key, value)
        digits = re.sub(r"\D", "", line)
        number = digits[0] + digits[-1]
        sum += int(number)
    print("Part 2: " + str(sum))


part1()
part2()
