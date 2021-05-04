def Num1330():
    parameter = input().split()
    A = int(parameter[0])
    B = int(parameter[1])

    print("==" if A == B else "<" if A < B else ">")
