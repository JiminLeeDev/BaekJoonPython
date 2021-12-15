def Num1712():
    result = 0

    inputs = [int(splitedInput) for splitedInput in input().split(" ")]

    fixedCosts = inputs[0]
    flexibleCosts = inputs[1]
    productPrice = inputs[2]
    profit = productPrice - flexibleCosts

    if profit <= 0:
        result = -1
    else:
        result = int(fixedCosts // profit + 1)

    print(result)


Num1712()
