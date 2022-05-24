# Password Generator

import random


def passwordGenerator(lenght):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    string = lower + upper + number
    password = "".join(random.sample(string, lenght))
    print('New Password:', password)


passwordGenerator(5)
