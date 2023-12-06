FILE_NAME = "input.txt"

with open(FILE_NAME) as f:
    calibration_sum = 0
    for line in f.readlines():
        calibration_value, last_digit = None, None
        for char in line:
            if not char.isdigit():
                continue

            if calibration_value is None:
                calibration_value = 10 * int(char)

            last_digit = char

        calibration_value += int(last_digit)
        calibration_sum += calibration_value

print(f"The calibration sum is {calibration_sum}")
