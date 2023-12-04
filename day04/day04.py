import os


def part1(data: list) -> None:
    sum = 0
    for d in data:
        win_num, card_num = d.split(":")[1].split("|")
        win_num = win_num.split()
        card_num = card_num.split()

        win_amount = 0
        for card in card_num:
            win_amount += win_num.count(card)

        if win_amount > 0:
            sum += pow(2, win_amount - 1)
    print(f"Part 1 : {sum}")


def part2(data: list) -> None:
    sum_cards = 0
    card_amount = {}
    for i, d in enumerate(data):
        win_num, card_num = d.split(":")[1].split("|")
        win_num = win_num.split()
        card_num = card_num.split()

        if i not in card_amount:
            card_amount[i] = 1

        for j in range(card_amount[i]):
            card_wins = 0
            for card in card_num:
                card_wins += win_num.count(card)
            for k in range(card_wins):
                if i + (k + 1) not in card_amount:
                    card_amount[i + (k + 1)] = 2
                else:
                    card_amount[i + (k + 1)] += 1

    sum_cards = sum(card_amount.values())

    print(f"Part 2 : {sum_cards}")


if __name__ == "__main__":
    print("Advent of Code: Day 04")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input.txt")
    with open(file_path) as f:
        data = f.read().splitlines()
        part1(data)
        part2(data)
