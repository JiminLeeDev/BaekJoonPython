def Get_Factorial(N, result):
    if N == 0:
        return result
    else:
        return Get_Factorial(N - 1, result * N)


def Num10872():
    N = int(input())

    result = Get_Factorial(N, 1)

    print(result)


Num10872()
