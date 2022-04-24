def merge_numbers(merged_numbers, unmerged_numbers, M):
    if len(merged_numbers) == M:
        result = str(merged_numbers)

        result = result.replace("[", "")
        result = result.replace("]", "")
        result = result.replace(",", "")

        print(result)

        return

    for idx in range(len(unmerged_numbers)):
        copied_numbers = unmerged_numbers.copy()
        copied_merge_numbers = merged_numbers.copy()
        copied_merge_numbers.append(copied_numbers.pop(idx))
        merge_numbers(copied_merge_numbers, copied_numbers, M)


def Num15649():
    inputs = [int(splitedInput) for splitedInput in input().split()]

    N = inputs[0]
    M = inputs[1]

    number_list = [n + 1 for n in range(N)]

    merge_numbers([], number_list, M)


Num15649()
