import random

def Game_Guess():

    def Human():
        print('Turn HUMAN')
        C_H = 0
        R = random.randint(1,99)
        int(R)
        print('----------------------------')
        while True:
            Num = int(input('Enter your guess: '))
            C_H += 1
            if Num == R:
                print(' !!!You Win!!! ')
                break
            elif R < Num:
                print('↓↓↓↓↓↓')
            elif R > Num:
                print('↑↑↑↑↑↑')
        print("Number of human guess:", C_H)
        return C_H

    def Bot():
        print('')
        print('Turn BOT')
        C_B = 0
        Num = int(input('Enter yor number: '))
        Max_R = 99
        Min_R = 1
        print('----------------------------')
        while True:
            R=random.randint(Min_R,Max_R)
            C_B += 1
            print('Guess: ',R)
            if R > Num:
                Max_R = R
            elif R < Num:
                Min_R = R
            elif R == Num:
                print('Oh OMG You Win!!!!!!')
                break
        print("Number of bot guess:", C_B)
        return C_B

    Turns_Human = Human()
    Turns_Bot = Bot()
    print('')
    print("Number of bot guess:", Turns_Bot)
    print("Number of human guess:", Turns_Human)
    print('')
    if Turns_Human < Turns_Bot:
        print('!!!! Win Human !!!!')
    elif Turns_Human > Turns_Bot:
        print('#### Win Bot ####')
    else:
        print('@#$# WTF !$#@@')

Game_Guess()