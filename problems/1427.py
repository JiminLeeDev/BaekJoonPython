def Num1427():
    result = ""

    n = str(int(input()))

    num_list = [0 for i in range(10)]

    for number in n:
        num_list[int(number)] += 1

    for number in range(len(num_list) - 1, -1, -1):
        for idx in range(num_list[number]):
            result += str(number)

    print(result)


Num1427()
