def FindFibonacciNumber(n):
    if n <= 1:
        return n

    return FindFibonacciNumber(n - 1) + FindFibonacciNumber(n - 2)


def Num10870():
    n = int(input())

    print(FindFibonacciNumber(n))


Num10870()