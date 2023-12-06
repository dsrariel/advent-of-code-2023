from collections import defaultdict

FILE_NAME = "input.txt"


def get_card_matches(numbers: str) -> int:
    number_lists = numbers.split(" | ", 1)

    winning_set = set(n for n in number_lists[0].split())

    matches = 0
    for number in number_lists[1].split():
        if number in winning_set:
            matches += 1

    return matches


def part2():
    total_cards = 0
    card_to_copies_count = defaultdict(lambda: 0)
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            card_and_numbers = line.split(": ", 1)
            card_number = int(card_and_numbers[0][len("Card ") :])
            matches = get_card_matches(card_and_numbers[1])

            copies_count = card_to_copies_count[card_number] + 1
            del card_to_copies_count[card_number]

            for i in range(matches):
                card_won = card_number + i + 1
                card_to_copies_count[card_won] += copies_count

            total_cards += copies_count

    print(f"The total cards you end up with is {total_cards}")


def part1():
    total_points = 0
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            card_and_numbers = line.split(": ", 1)

            winning_numbers_count = get_card_matches(card_and_numbers[1])

            if winning_numbers_count > 0:
                card_points = 2 ** (winning_numbers_count - 1)
                total_points += card_points

    print(f"The cards are worth {total_points} points.")


if __name__ == "__main__":
    part1()
    part2()
