from functools import cmp_to_key


def Num1422():
    inputs = input().split(" ")

    k = int(inputs[0])
    n = int(inputs[1])

    max = 0
    result = ""
    numbers = []

    for number in range(k):
        inputNumber = input()

        if int(max) < int(inputNumber):
            max = inputNumber

        numbers.append(inputNumber)

    for idx in range(n - k):
        numbers.append(max)

    numbers.sort(key=cmp_to_key(lambda x, y: -1 if x + y > y + x else 1))

    for number in numbers:
        result += str(number)

    print(result)


Num1422()
