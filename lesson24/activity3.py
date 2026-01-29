# power set of a set

# 3-> 2^3=8

import math


def f1(s, size):  # [4,9,6],3

    psize = (int)(math.pow(2, size))  # 8

    x = 0

    y = 0

    for x in range(psize):  # 8

        for y in range(size):  # 3

            if ((x & (1 << y)) > 0):

                print(s[y], end="")

            print("")


size = int(input("Enter array size: "))

set = []

for i in range(size):

    n = input("Enter an element : ")

set.append(n)  # 4,9,6

f1(set, len(set))  # [4,9,6],3

'''

p=8, x : 0 to 7

s=3, y : 0 to 2

x=0, 1,2

001 & 00,

010

'''
