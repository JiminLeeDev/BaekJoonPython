def Num1181():
    words = [input() for word in range(int(input()))]
    words = list(set(words))
    words = sorted(words)
    words = sorted(words, key=lambda word: len(word))

    for word in words:
        print(word)


Num1181()
