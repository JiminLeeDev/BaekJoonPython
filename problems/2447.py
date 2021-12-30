def draw_patern(n, src):
    result = []

    if n == 1:
        return src

    for y in range(3):
        for x in src:
            if y == 1:
                result.append(x + " " * len(x) + x)
            else:
                result.append(x * 3)

    return draw_patern(n // 3, result)


def Num2447():
    n = int(input())
    
    result = draw_patern(n, ["*"])

    for line in result:
        print(line)


Num2447()
