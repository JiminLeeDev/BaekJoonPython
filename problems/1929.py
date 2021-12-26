def Num1929():
    inputs = [int(splitedInput) for splitedInput in input().split()]

    M = inputs[0]
    N = inputs[1]

    numbers = [True for idx in range(N + 1)]

    multiMax = int(N ** 0.5) + 1

    numbers[1] = False

    for idx in range(2, multiMax):
        if numbers[idx]:
            for multiIdx in range(idx + idx, N + 1, idx):
                numbers[multiIdx] = False

    for idx in range(M, N + 1):
        if numbers[idx]:
            print(int(idx))


Num1929()
