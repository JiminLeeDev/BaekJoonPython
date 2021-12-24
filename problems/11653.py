def Num11653():
    N = int(input())

    idx = 2

    while N != 1:
        if N % idx == 0:
            N /= idx

            print(idx)
        else:
            idx += 1


Num11653()
