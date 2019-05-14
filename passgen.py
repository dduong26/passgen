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
    mix = (string.ascii_letters + string.digits)

    while count < length:
        passlist.append(mix[random.randrange(0, 62)])
        count += 1
    return(passlist)

length = int(input("Length of password? "))
total = genpass(length)
print("".join(total))
