def part1():
    sum = 0
    with open("2.txt", "r") as f:
        lines = f.read().splitlines()
        red = 12
        green = 13
        blue = 14

        ids = []

        for line in lines:
            line = line.replace("Game ", "")
            id, sets = line.split(":")
            set = sets.split(";")
            is_invalid = False
            for s in set:
                cubes = s.split(",")
                for c in cubes:
                    values = c.split(" ")[1:]
                    match values[1]:
                        case "red":
                            if int(values[0]) > red:
                                is_invalid = True
                        case "green":
                            if int(values[0]) > green:
                                is_invalid = True
                        case "blue":
                            if int(values[0]) > blue:
                                is_invalid = True
                    if is_invalid:
                        break
                if is_invalid:
                    break
            if is_invalid:
                continue
            ids.append(id)
            sum += int(id)
    print(f"Part 1: {sum}")


def part2():
    sum = 0
    with open("2.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            red = 0
            green = 0
            blue = 0
            line = line.replace("Game ", "")
            id, sets = line.split(":")
            set = sets.split(";")
            for s in set:
                cubes = s.split(",")
                for c in cubes:
                    values = c.split(" ")[1:]
                    match values[1]:
                        case "red":
                            if int(values[0]) > red:
                                red = int(values[0])
                        case "green":
                            if int(values[0]) > green:
                                green = int(values[0])
                        case "blue":
                            if int(values[0]) > blue:
                                blue = int(values[0])
            sum += red * green * blue
    print(f"Part 2: {sum}")


part1()
part2()
