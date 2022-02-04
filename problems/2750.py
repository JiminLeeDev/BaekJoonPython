def Num2750():
    n = int(input())

    numbers = [int(input()) for idx in range(n)]

    for idx1 in range(n):
        for idx2 in range(n):
            if numbers[idx1] < numbers[idx2]:
                temp = numbers[idx1]
                numbers[idx1] = numbers[idx2]
                numbers[idx2] = temp

    for number in numbers:
        print(number)


Num2750()
