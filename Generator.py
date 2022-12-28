import string
import random


def Generate_Password(num):
    password = ''

    for n in range(num):
        while True:
            x = random.randint(0, 94)
            if string.printable[x] != ' ':
                break
        password += string.printable[x]
    return password


print(Generate_Password(20))