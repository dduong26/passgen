#! /usr/bin/env python

"""
Author: David Duong
Date: May 13th 2019
About: Learning Python so I created a random password generator
"""

import string
import random

def genpass (length):
    count = 0
    passlist = []
    letters = string.ascii_letters
    numbers = string.digits

    while count < length:
        strascii = string.ascii_letters[random.randrange(0, 52)]
        digits = string.digits[random.randrange(0, 10)]
        passlist.append(strascii)
        passlist.append(digits)
        count += 1
    return(passlist)

length = int(input("Length of password? "))
total = genpass(length)
print("".join(total))
