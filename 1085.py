def Num1085():
    parameter = input().split()
    x = int(parameter[0])
    y = int(parameter[1])
    w = int(parameter[2])
    h = int(parameter[3])

    distList.append(x)
    distList.append(w - x)
    distList.append(h - y)
    distList.append(y)

    result = min(distList)

    print(result)


Num1085()
