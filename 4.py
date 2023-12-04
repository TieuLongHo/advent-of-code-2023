def part1():
    sum = 0
    with open("4.txt") as f:
        data = f.read().splitlines()
        for d in data:
            win_num, card_num = d.split(":")[1].split("|")
            win_num = list(map(int, list(filter(None, win_num.split(" ")))))
            card_num = list(map(int, list(filter(None, card_num.split(" ")))))

            win_amount = 0
            for card in card_num:
                win_amount += win_num.count(card)

            if win_amount > 1:
                sum += pow(2, win_amount - 1)
            else:
                sum += win_amount
    print(f"Part 1 : {sum}")


def part2():
    sum_cards = 0
    card_amount = {}
    with open("4.txt") as f:
        data = f.read().splitlines()
        for i, d in enumerate(data):
            win_num, card_num = d.split(":")[1].split("|")
            win_num = list(map(int, list(filter(None, win_num.split(" ")))))
            card_num = list(map(int, list(filter(None, card_num.split(" ")))))

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


part1()
part2()
