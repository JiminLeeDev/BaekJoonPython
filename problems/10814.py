def Num10814():
    people = [input().split(" ") for data in range(int(input()))]
    ages = list(set([person[0] for person in people]))

    result_dict = {}

    ages.sort(key=lambda age: int(age))

    for age in ages:
        result_dict[age] = []

    for person in people:
        result_dict.get(person[0]).append(person[1])

    for same_age_people in result_dict.items():
        for person in same_age_people[1]:
            print(f"{same_age_people[0]} {person}")


Num10814()
