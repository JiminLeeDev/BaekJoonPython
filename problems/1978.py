def Num1978():
    N = int(input())

    result = 0

    for splitedNumber in input().split():
        isPrimeNumber = True

        splitedNumber = int(splitedNumber)

        if splitedNumber == 1:
            continue

        for divideNumber in range(2, splitedNumber):
            if splitedNumber % divideNumber == 0:
                isPrimeNumber = False

                break

        if isPrimeNumber:
            result += 1

    print(result)


Num1978()
