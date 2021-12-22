def Num2581():
    M = int(input())
    N = int(input())

    minPrimeNum = 0
    sumPrimeNum = 0

    primeNums = []

    for dividend in range(M, N+1):
        if dividend == 1:
            continue

        primeNums.append(dividend)

        sumPrimeNum += dividend

        for divisor in range(2, dividend):
            if dividend % divisor == 0:
                primeNums.pop()

                sumPrimeNum -= dividend

                break

    if len(primeNums) == 0:
        print("-1")
    else:
        minPrimeNum = primeNums[0]
        sumPrimeNum = sum(primeNums)

        print(str(sumPrimeNum))
        print(str(minPrimeNum))


Num2581()
