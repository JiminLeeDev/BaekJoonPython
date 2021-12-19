def Num3009():
    coordinate = [
        [int(splitedInput) for splitedInput in input().split()] for i in range(3)
    ]

    xSet = [coordinate[i][0] for i in range(3)]
    ySet = [coordinate[i][1] for i in range(3)]

    x = 0
    y = 0

    for idx in range(3):
        if xSet.count(xSet[idx]) == 1:
            x = xSet[idx]

        if ySet.count(ySet[idx]) == 1:
            y = ySet[idx]

    print(str(x) + " " + str(y))


Num3009()
