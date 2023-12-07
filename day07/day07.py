import os


def part1(data: list, cards: list) -> None:
    print(f"Part 1: {get_sorted_hand(data, cards, False)}")


def get_sorted_hand(data: list, cards: list, part2: bool) -> int:
    new_hand = {}
    for hand in data:
        hand_type = find_hand_type(hand[0], cards, part2)
        if new_hand.get(hand_type) is None:
            new_hand[hand_type] = [[hand[0], hand[1], hand_type]]
            continue
        new_hand[hand_type].append([hand[0], hand[1], hand_type])
    new_hand = dict(sorted(new_hand.items()))
    hand_list = []
    for key in new_hand.keys():
        hand_list.insert(0, new_hand[key])
    for hand_type in hand_list:
        quicksort(hand_type, 0, len(hand_type) - 1, cards)

    flat_hands = [item for sublist in hand_list for item in sublist]

    winning = 0
    for i, hands in enumerate(flat_hands):
        winning += int(hands[1]) * (i + 1)
    return winning


def part2(data: list, cards: list) -> None:
    print(f"Part 2: {get_sorted_hand(data, cards, True)}")


def partition(arr: list, low: int, high: int, cards: list) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if not is_bigger(arr[j][0], pivot[0], cards):
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def quicksort(arr: list, low: int, high: int, cards: list) -> None:
    if low < high:
        pi = partition(arr, low, high, cards)
        quicksort(arr, low, pi - 1, cards)
        quicksort(arr, pi + 1, high, cards)


def is_bigger(hand1: list, hand2: list, cards: list) -> bool:
    for i in range(len(hand1)):
        if cards.index(hand1[i]) < cards.index(hand2[i]):
            return True
        elif cards.index(hand1[i]) == cards.index(hand2[i]):
            continue
        else:
            return False
    return False


def find_hand_type(hand: str, cards: list, part2: bool) -> int:
    found_cards = {}
    for card in cards:
        if sum(found_cards.values()) == 5:
            break
        if hand.count(card) != 0:
            found_cards[card] = hand.count(card)
    if part2:
        biggest = sorted(found_cards, key=found_cards.get)[-1]
        if biggest != "J" and "J" in found_cards:
            found_cards[biggest] += found_cards.pop("J")
        elif biggest == "J" and found_cards["J"] != 5:
            found_cards[
                sorted(found_cards, key=found_cards.get)[-2]
            ] += found_cards.pop("J")

    hand = list(found_cards.values())
    hand.sort(reverse=True)

    return hand_types.index(hand)


if __name__ == "__main__":
    print("Advent of Code: Day 06")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input.txt")
    with open(file_path) as f:
        data = f.read().splitlines()
        cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        cards2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
        hand_types = [
            [5],
            [4, 1],
            [3, 2],
            [3, 1, 1],
            [2, 2, 1],
            [2, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        hands = []
        for d in data:
            hands.append(d.split())

        part1(hands, cards)
        part2(hands, cards2)
