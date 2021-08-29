def Num1193():
    result = ""
    x = int(input())
    line = 0
    sum = 0
    mod = 0

    if x == 1:
        result = "1/1"

        print(result)

        return

    for i in range(1, x + 1):
        sum += i

        if x - sum <= 0:
            line = i
            mod = sum - x + 1

            break

    if line % 2 == 0:
        result = str(line - mod + 1) + "/" + str(mod)
    else:
        result = str(mod) + "/" + str(line - mod + 1)

    print(result)


Num1193()
