def Num10250():
    T = int(input())

    for testcase in range(T):
        parameter = input().split()
        H = int(parameter[0])
        N = int(parameter[2])

        if N % H == 0:
            floor = H
            room = N // H
        else:
            floor = N % H
            room = N // H + 1

        result = floor * 100 + room

        print(str(result))
