def Num2884():
    inputs = [int(splitedInput) for splitedInput in input().split()]
    h = inputs[0]
    m = inputs[1]
    preTime = 45
    resultM = 0
    resultH = 0

    if m - preTime < 0:
        resultM = 60 + (m - preTime)

        if h == 0:
            resultH = 23
        else:
            resultH = h - 1
    else:
        resultH = h
        resultM = m - preTime

    result = str(resultH) + " " + str(resultM)

    print(result)


Num2884()
