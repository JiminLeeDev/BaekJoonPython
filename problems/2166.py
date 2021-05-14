def Num2166():
    N = int(input())
    coordinate = [[int(i) for i in input().split()] for i in range(N)]
    xSet = [i[0] for i in coordinate]
    ySet = [i[1] for i in coordinate]
    sum = 0

    for i in range(N - 1):
        sum += xSet[i] * ySet[i + 1] - xSet[i + 1] * ySet[i]

    sum += xSet[N - 1] * ySet[0] - xSet[0] * ySet[N - 1]
    result = abs(sum) / 2

    print(round(result, 1))


Num2166()
