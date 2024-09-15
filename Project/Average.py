def Average():

    Sum_N=0
    float(Sum_N)
    Count_N=0
    float(Count_N)
    Average_N=0
    float(Average_N)
    while True:
        Number=float(input('Enter your Number: '))
        if Number == -1:
            break
        Count_N = Count_N +1
        Sum_N = Number + Sum_N
    Average_N = Sum_N / Count_N
    print('Average: ',Average_N)

Average()