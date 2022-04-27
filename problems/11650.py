def Num11650():
    n = int(input())

    coordinates = []

    for idx in range(n):
        coordinates.append([int(number) for number in input().split(" ")])

    coordinates = sorted(coordinates)

    for coordinate in coordinates:
        print(str(coordinate[0]) + " " + str(coordinate[1]))


Num11650()
