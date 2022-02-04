def move(n, a, b, c):
    if n == 1:
        print(str(a) + " " + str(c))
    else:
        move(n - 1, a, c, b)
        print(str(a) + " " + str(c))
        move(n - 1, b, a, c)


def Num11729():
    n = int(input())

    print(2 ** n - 1)
    move(n, 1, 2, 3)


Num11729()
