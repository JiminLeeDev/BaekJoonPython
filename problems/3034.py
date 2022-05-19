def Num3034():
    inputs = [int(splitedInput) for splitedInput in input().split(' ')]

    N = inputs[0]
    W = inputs[1]
    H = inputs[2]

    squaredDiagonalSize = W * W +  H * H

    for idx in range(N):
        matchSize = int(input())

        matchSize *= matchSize

        if(squaredDiagonalSize >= matchSize):
            print("DA")
        else:
            print("NE")

Num3034()