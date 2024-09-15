import string

def TextLS():
    Text_String = input("Enter Your Text: ")
    lowercases = string.ascii_lowercase
    output=""

    for char in Text_String:
        if char in lowercases:
            output += char.upper()

        else:
            output += char.lower()
    print(output)

TextLS()