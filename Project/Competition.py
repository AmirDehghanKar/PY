import random
def Competition():

    Horses = {
    "Horse_1": 0,
    "Horse_2": 0,
    "Horse_3": 0,
    "Horse_4": 0
    }

    Horse = "|==|->"
    RunA = " "
    counter = 10

    flag = True
    winner_name = None

    while flag:
        for key in Horses:
            Horses[key] += random.randint(1, 4)
            if Horses[key] > 27:
                flag = False
                winner_name = key

        for key in Horses:
            s = str(Horses[key]) + (RunA * (Horses[key]-1)) + Horse
            c = 27 - len(s) # -> 5
            if c > 0:
                s += (" " * (c-1)) + "|"

            elif c < 0:
                lst = list(s)
                lst[27] = "|"
                s = "".join(lst)

            print(s)
        print("\n= = = = = = = = = = = = = =\n")
    print(f"Hurray, {winner_name.capitalize()} win!!")

Competition()

#  ______________
# < I'm horse... >
#  --------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
