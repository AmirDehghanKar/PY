import random

def Calculation():
    Result1 = 0
    Result2 = 0
    Result3 = 0
    Operator = ['+','-','*']
    Number1 = int(random.randint(1,9))
    Input0 = random.choice(Operator)
    Number2 = int(random.randint(1,9))
    print (Number1,Input0,Number2)
    Result0 = int (input('  = '))
    Result1 = Result0

    Output1 = Number1 - Number2
    Result2 = Number1 + Number2
    Output3 = Number1 * Number2

    if Input0 == '+' and Result1 == Result2:
        print('✅✅✅✅')
    elif Input0 == '-' and Result1 == Output1:
        print('✅✅✅✅')
    elif Input0 == '*' and Result1 == Output3:
        print('✅✅✅✅')
    else:
        print('❌❌❌❌')

Calculation()