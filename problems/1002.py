import math


def Num1002():
    T = int(input())

    while T != 0:
        T -= 1

        parameters = [int(parameter) for parameter in input().split()]

        dist = math.sqrt(
            (parameters[0] - parameters[3]) ** 2 + (parameters[1] - parameters[4]) ** 2
        )

        radiusTuple = sorted((parameters[2], parameters[5]))

        if dist == 0 and radiusTuple[0] - radiusTuple[1] == 0:
            print(-1)

            continue

        if (
            dist > radiusTuple[1] - radiusTuple[0]
            and dist < radiusTuple[0] + radiusTuple[1]
        ):
            print(2)

            continue

        if (
            radiusTuple[0] + radiusTuple[1] == dist
            or radiusTuple[1] - radiusTuple[0] == dist
        ):
            print(1)

            continue

        if (
            radiusTuple[0] + radiusTuple[1] < dist
            or radiusTuple[1] - radiusTuple[0] > dist
        ):
            print(0)

            continue


Num1002()
