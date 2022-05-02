def Num5086():
    numbers = [int(number) for number in input().split(" ")]

    while numbers[0] != 0 or numbers[1] != 0:
        if numbers[1] % numbers[0] == 0:
            print("factor")
        elif numbers[0] % numbers[1] == 0:
            print("multiple")
        else:
            print("neither")

        numbers = [int(number) for number in input().split(" ")]


Num5086()
