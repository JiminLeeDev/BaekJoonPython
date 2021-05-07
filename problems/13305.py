def Num13305():
    N = [0] * int(input())
    roads = [int(i) for i in input().split()]
    cities = [int(i) for i in input().split()]
    miniumCity = cities[0]
    result = 0

    for i in range(1, len(N)):
        N[i - 1] = miniumCity * roads[i - 1]

        if miniumCity < cities[i]:
            i += 1
        else:
            miniumCity = cities[i]

    result = sum(N)

    print(result)


Num13305()