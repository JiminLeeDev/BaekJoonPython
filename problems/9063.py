def Num9063():
    N = int(input())

    min_coordinate = [10001, 10001]
    max_coordinate = [-10001, -10001]

    for i in range(N):
        coordinate = [
            int(unparsed_coordinate) for unparsed_coordinate in input().split(" ")
        ]

        if min_coordinate[0] > coordinate[0]:
            min_coordinate[0] = coordinate[0]

        if max_coordinate[0] < coordinate[0]:
            max_coordinate[0] = coordinate[0]

        if min_coordinate[1] > coordinate[1]:
            min_coordinate[1] = coordinate[1]

        if max_coordinate[1] < coordinate[1]:
            max_coordinate[1] = coordinate[1]

    width = abs(max_coordinate[0] - min_coordinate[0])
    height = abs(max_coordinate[1] - min_coordinate[1])
    result = width * height

    print(result)


Num9063()
