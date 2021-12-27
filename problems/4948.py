def Num4948():
    n = int(input())

    while n != 0:
        result = 0

        nums = [True] * (n * 2 + 1)

        for idx in range(2, int(n * 2 ** 0.5) + 1):
            if nums[idx] == True:
                for multiIdx in range(idx * 2, n * 2 + 1, idx):
                    nums[multiIdx] = False

        for idx in range(len(nums)):
            if idx > n and nums[idx] == True:
                result += 1

        print(result)

        n = int(input())


Num4948()
