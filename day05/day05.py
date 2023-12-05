import os


def part1(data: list) -> None:
    destination = []
    for seed in data[0][0]:
        source = seed
        for maps in data[1:]:
            for map in maps:
                if source not in range(map[1], map[1] + map[2]):
                    continue
                offset = source - map[1]
                source = map[0] + offset
                break
        destination.append(source)
    destination.sort()
    print(f"Part 1: {destination[0]}")


def part2(data: list) -> None:
    current_ranges = []
    mapped_ranges = []
    seed_ranges = []
    current_seed = []
    for i, seeds in enumerate(data[0][0]):
        if (i + 1) % 2 != 0:
            current_seed.append(seeds)
        else:
            current_seed.append(current_seed[0] + seeds)
            seed_ranges.append(current_seed)
            current_seed = []

    for maps in data[1:]:
        for map in maps:
            for seed in seed_ranges:
                ac_range = range(map[1], map[1] + map[2])
                # right
                if seed[0] in ac_range and seed[1] not in ac_range:
                    offset = seed[0] - map[1]
                    mapped_ranges.append([map[0] + offset, map[0] + map[2]])
                    current_ranges.append([map[1] + map[2], seed[1]])
                # left
                elif seed[0] not in ac_range and seed[1] in ac_range:
                    offset = seed[1] - map[1]
                    current_ranges.append([seed[0], map[1]])
                    mapped_ranges.append([map[0], map[0] + offset])
                # inside
                elif seed[0] in ac_range and seed[1] in ac_range:
                    offset = seed[0] - map[1]
                    mapped_ranges.append(
                        [map[0] + offset, map[0] + offset + (seed[1] - seed[0])]
                    )
                # around
                elif map[1] > seed[0] and (map[1] + map[2]) < seed[1]:
                    current_ranges.append([seed[0], map[1]])
                    mapped_ranges.append([map[0], map[0] + map[2]])
                    current_ranges.append([map[1] + map[2], seed[1]])
                else:
                    current_ranges.append(seed)
            seed_ranges = current_ranges
            current_ranges = []
        seed_ranges.extend(mapped_ranges)
        mapped_ranges = []

    destination = sorted(seed_ranges, key=lambda x: (x[0], -x[1]))

    print(f"Part 2: {destination[0][0]}")


if __name__ == "__main__":
    print("Advent of Code: Day 05")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input.txt")
    with open(file_path) as f:
        data = f.read().splitlines()
        # seeds, seed-to-soil, soil-to-fertilizer, fertilizer-to-water, water-to-light, light-to-temp, temp-to-humidity, humidity-to-location
        sorted_data = []
        first = True
        change = False
        current_data = []
        for d in data:
            if first:
                d = d.split(":")[1]
                first = False
            if change:
                change = False
                continue
            if d == "":
                change = True
                sorted_data.append(current_data)
                current_data = []
                continue

            current_data.append([eval(i) for i in d.split()])
        sorted_data.append(current_data)

        part1(sorted_data)
        part2(sorted_data)
