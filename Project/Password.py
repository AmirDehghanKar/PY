import random
import string

def Password():

    chars = string.ascii_letters + string.digits + string.punctuation
    Num = int(input("Enter Your Number: "))
    Password = ""

    for i in range(Num):
        C = random.choice(chars)
        Password += C
    print("Your Pass: ",Password)

Password()