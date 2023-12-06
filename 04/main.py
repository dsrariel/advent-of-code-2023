FILE_NAME = "input.txt"


def main():
    total_points = 0
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            card_and_numbers = line.split(": ", 1)
            number_lists = card_and_numbers[1].split(" | ", 1)

            winning_set = set(n for n in number_lists[0].split())

            winning_numbers_count = 0
            for number in number_lists[1].split():
                if number in winning_set:
                    winning_numbers_count += 1

            if winning_numbers_count > 0:
                card_points = 2 ** (winning_numbers_count - 1)
                total_points += card_points

    print(f"The cards are worth {total_points} points.")


if __name__ == "__main__":
    main()
