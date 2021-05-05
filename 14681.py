def Num14681():
    x = int(input())
    y = int(input())
    result = 0

    if x > 0:
        if y > 0:
            result = 1
        else:
            result = 4
    else:
        if y < 0:
            result = 3
        else:
            result = 2

    print(str(result))
