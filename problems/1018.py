def Num1018():
    parameter = [int(i) for i in input().split()]
    N = parameter[0]
    M = parameter[1]
    board = [[char for char in input()] for string in range(0, N)]
    result = 0
    kernelBoard = []
    blackTurn = True

    for y in range(0, 8):
        kernelBoard.append([])

        for x in range(0, 8):
            if blackTurn == True:
                kernelBoard[y].append("B")
                blackTurn = False
            else:
                kernelBoard[y].append("W")
                blackTurn = True

        blackTurn = False if blackTurn else True

    score = []

    for cY in range(0, N - 7):
        for cX in range(0, M - 7):
            score += calcScore(cX, cY, board, kernelBoard)

    result = min(score)

    print(result)


def calcScore(cX, cY, board, kernelBoard):
    result = [0]

    for y in range(0, 8):
        for x in range(0, 8):
            result[0] += 1 if board[cY + y][cX + x] != kernelBoard[y][x] else 0

    result.append(64 - result[0])

    return result


Num1018()