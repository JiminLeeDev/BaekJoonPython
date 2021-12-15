def Num2798():
    parameter = input().split()
    N = int(parameter[0])
    M = int(parameter[1])
    parameter = input().split()
    cards = []
    result = 0

    for card in parameter:
        cards.append(int(card))

    preIndexScore = M

    for compareCard1 in cards:
        for compareCard2 in cards:
            if compareCard1 == compareCard2:
                continue

            for compareCard3 in cards:
                if compareCard1 == compareCard3 or compareCard2 == compareCard3:
                    continue

                score = compareCard1 + compareCard2 + compareCard3

                if M >= score and M - score <= preIndexScore:
                    preIndexScore = M - score
                    result = score

    print(result)

Num2798()