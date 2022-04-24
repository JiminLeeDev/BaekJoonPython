from collections import Counter
import numbers
import sys


def Num2108():
    number_cnt = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for n in range(number_cnt)]

    numbers.sort()

    average_value = round(sum(numbers) / number_cnt)
    center_value = numbers[number_cnt // 2]
    mode_values = Counter(numbers).most_common()
    mode_value = 0

    if len(mode_values) == 1 or mode_values[0][1] != mode_values[1][1]:
        mode_value = mode_values[0][0]
    else:
        mode_value = mode_values[1][0]

    range_value = numbers[len(numbers) - 1] - numbers[0]

    print(average_value)
    print(center_value)
    print(mode_value)
    print(range_value)


Num2108()
