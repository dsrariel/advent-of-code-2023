from dataclasses import dataclass
from typing import List, Optional

FILE_NAME = "input.txt"


@dataclass
class Race:
    time: int
    record: int

    def count_ways_to_win(self) -> Optional[int]:
        """returns the count of ways to beat the record in the given time.

        Our race is modeled by the following equations and inequalities:
            speed = holding_time
            distance = speed * remaining_time
            time = remaining_time + holding_time

            remaining_time >= 0
            holding_time >= 0

        The equation we want to solve is the following:
            distance > record

        That is:
            holding_time * remaining_time > record
            holding_time * (time - holding_time) > record
            - holding_time ** 2 + time * holding_time - record > 0

        This means we have an open down parabola and we win in the holding_time interval between the
        two roots (x_1 and x_2, where x_2 > x_1) of the quadratic equation (given record value is
        not too high).

        The count of the ways to win will be the number of integers between the roots. If we wore to
        include the roots, that number would be x_2 - x_1 + 1 ways of winning. We know that
        x_1 + x_2 = -(b/a), which means x_1 + x_2 = time. So, the count of ways to win would be:
            time - 2*x_1 + 1

        If we insert the first number that satisfies the inequality, we will select a more
        restricted interval between our root. This is exactly what we want for this problem, since
        the roots should not count as  ways of winning and they may also not be ints.
        """
        for holding_time in range(self.time):
            remaining_time = self.time - holding_time
            distance = holding_time * remaining_time
            if distance > self.record:
                return self.time - 2 * holding_time + 1
        return None


def load_input() -> List[Race]:
    times, distances = [], []
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            if line.startswith("Time:"):
                times = [int(n) for n in line[len("Time: ") :].strip().split()]

            if line.startswith("Distance:"):
                distances = [int(n) for n in line[len("Distance: ") :].strip().split()]

    return [Race(t, d) for t, d in zip(times, distances)]


def load_input_as_part_2() -> Race:
    time, distance = 0, 0
    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines():
            if line.startswith("Time:"):
                time = int(line[len("Time: ") :].strip().replace(" ", ""))

            if line.startswith("Distance:"):
                distance = int(line[len("Distance: ") :].strip().replace(" ", ""))

    return Race(time, distance)


def part2():
    race = load_input_as_part_2()
    print(f"The ways to win are {race.count_ways_to_win()}.")


def part1():
    races = load_input()
    ways_to_win_multiplication = 1
    for race in races:
        ways_to_win = race.count_ways_to_win()
        if ways_to_win is not None:
            ways_to_win_multiplication *= ways_to_win

    print(f"The multiplication of the ways to win is {ways_to_win_multiplication}.")


if __name__ == "__main__":
    part1()
    part2()
