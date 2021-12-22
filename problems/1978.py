def Num1978():
    N = int(input())

    result = 0

    for splitedNumber in input().split():
        number = int(splitedNumber)

        isPrimeNumber = True

        for divideNumber in range(2, number):
            if number % divideNumber == 0:
                isPrimeNumber = False

                break

        if isPrimeNumber:
            result += 1

    print(result)


Num1978()
