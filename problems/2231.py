def Num2231():
    N = int(input())

    constructor = []
    result = 0

    for i in range(N):

        placeValue = sum([int(n) for n in str(N - i)])

        if N - i + placeValue == N:
            constructor.append(N - i)

    if not constructor:
        result = 0
    else:
        result = min(constructor)

    print(result)


Num2231()