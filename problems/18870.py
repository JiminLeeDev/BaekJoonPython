def Num18870():
    N = int(input())

    numbers = [int(number) for number in input().split(" ")]
    sorted_number_set = sorted(list(set(numbers)))
    sorted_number_dict = {}

    result = ""

    for idx in range(len(sorted_number_set)):
        sorted_number_dict[sorted_number_set[idx]] = idx

    for number in numbers:
        result += str(sorted_number_dict[number]) + " "

    print(result)


Num18870()
