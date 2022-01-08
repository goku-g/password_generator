# program that generate random password

import random

# variables

alphabets = "abcdefghijklmnopqrstuvwxyz"

numericals = "0123456789"

symbols = r"!@$_%^&*-+=.>,</?_\|`~"
value = True

def password_generate(password):

    i = random.randrange(0,len(alphabets)-1)
    password.append(alphabets[i].upper())

    i = random.randrange(0,len(alphabets)-1)
    password.append(alphabets[i].upper())

    i = random.randrange(0,len(alphabets)-1)
    password.append(alphabets[i].upper())

    i = random.randrange(0,len(alphabets)-1)
    password.append(alphabets[i].upper())

    i = random.randrange(0,len(numericals)-1)
    password.append(numericals[i])

    i = random.randrange(0,len(numericals)-1)
    password.append(numericals[i])

    i = random.randrange(0,len(numericals)-1)
    password.append(numericals[i])

    i = random.randrange(0,len(symbols)-1)
    password.append(symbols[i])

    i = random.randrange(0,len(symbols)-1)
    password.append(symbols[i])

    i = random.randrange(0,len(symbols)-1)
    password.append(symbols[i])

    i = random.randrange(0,len(symbols)-1)
    password.append(symbols[i])

    random.shuffle(password)

    delim = ""
    string = delim.join(password)

    return string

flag = input("Do you want to generate a password?(Y/N)")

if flag != 'N' or flag != 'n':
    
    while value:
        value = False

        word = password_generate([])

        print("Your password is : {}".format(word))

        value = not(input("Another password?? ('q' for calcel)") == "q")

