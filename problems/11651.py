def Num11651():
    n = int(input())

    coordinates = []

    for idx in range(n):
        coordinates.append([int(number) for number in input().split(" ")])

    coordinates = sorted(coordinates, key=lambda x: (x[1], x[0]))

    for coordinate in coordinates:
        print(str(coordinate[0]) + " " + str(coordinate[1]))


Num11651()
