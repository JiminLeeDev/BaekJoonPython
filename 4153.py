def Num4153():
    while True:
        testcase = input().split()

        if testcase.count("0") == 3:
            return

        triangle = [int(t) for t in testcase]

        triangle.sort()

        if triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2:
            print("right")
        else:
            print("wrong")


Num4153()