def Num1436():
    sixNum = "666"
    result = 665
    idx = 0
    n = int(input())

    while idx < n:
        if sixNum in str(result):
            idx += 1

        result += 1

    result -= 1

    print(result)


Num1436()
