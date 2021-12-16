def Num2839():
    result = 0
    smallBag = 3
    largeBag = 5
    n = int(input())

    while True:
        if n % largeBag == 0:
            result += n // largeBag
            n = 0
        else:
            result += 1
            n -= smallBag

        if n <= 0:
            break

    if n < 0:
        result = -1

    print(result)


Num2839()
