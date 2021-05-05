def Num1085():
    parameter = input().split()
    x = int(parameter[0])
    y = int(parameter[1])
    w = int(parameter[2])
    h = int(parameter[3])

    result = min([x, w - x, h - y, y])

    print(result)


Num1085()
