def Figures():

    Num = 0
    def Numbers():
        Num = input('Enter yor number: ')
        Max_N = max(Num)
        print('Big number: ', Max_N)
        Min_N = min(Num)
        print('Min number: ', Min_N)

    while True:
        Numbers()
        break

Figures()