def Num11047():
    result = 0
    parameter = [int(num) for num in input().split()]
    N = parameter[0]
    K = parameter[1]
    moneyValues = sorted([int(input()) for i in range(N)], reverse=True)

    for moneyValue in moneyValues:
        if K % moneyValue == 0:
            result += K // moneyValue
            print(result)

            break
        elif K >= moneyValue:
            result += K // moneyValue
            K = K % moneyValue


Num11047()