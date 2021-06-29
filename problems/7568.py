def Num7568():
    N = int(input())
    bodyList = [[int(i) for i in input().split()] for i in range(N)]

    result = ""
    grades = []

    for body1 in bodyList:
        grade = 0

        for body2 in bodyList:
            if body1[0] < body2[0] and body1[1] < body2[1]:
                grade += 1

        grades.append(grade + 1)

    for grade in grades:
        result += str(grade) + " "

    print(result)


Num7568()