def Num2292():
    result = 0

    n = int(input())

    sum = 1

    while n > sum:
        result += 1
        sum += 6 * result

    result += 1

    print(result)


Num2292()
