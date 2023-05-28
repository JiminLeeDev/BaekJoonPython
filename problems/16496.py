from functools import cmp_to_key


def Num16496():
    n = int(input())

    numbers = [number for number in input().split(" ")]

    result = ""

    for number in sorted(
        numbers, key=cmp_to_key(lambda x, y: -1 if x + y > y + x else 1)
    ):
        result += number

    print(0 if result[0] == "0" else result)


Num16496()
