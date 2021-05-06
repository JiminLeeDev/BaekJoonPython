def Num9029():
    nums = [True] * 10000

    for n in range(2, int(len(nums) ** 0.5) + 1):
        if nums[n] == True:
            for compositionNum in range(n + n, len(nums), n):
                nums[compositionNum] = False

    testcase = int(input())

    for t in range(testcase):
        n = int(input())
        numberOfN = [(i, n - i) for i in range(1, n // 2 + 1)]
        goldbachNums = []

        for i in numberOfN:
            a = i[0]
            b = i[1]

            if nums[a] and nums[b]:
                goldbachNums.append((a, b, (a - b) ** 2))

        goldbachNums.sort(key=lambda goldbachNum: int(goldbachNum[2]))
        result = str(goldbachNums[0][0]) + " " + str(goldbachNums[0][1])

        print(result)


Num9029()
