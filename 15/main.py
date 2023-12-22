FILE_NAME = "input.txt"


def load_input() -> list[str]:
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            return line.split(",")


def hashing(string: str) -> int:
    result = 0
    for c in string:
        result += ord(c)
        result *= 17
        result %= 256

    return result


def part_one():
    sequences = load_input()
    print(f"The sum of the hashes is {sum(map(hashing, sequences))}.")


if __name__ == "__main__":
    part_one()
