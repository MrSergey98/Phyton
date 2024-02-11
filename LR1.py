import math
import random

# f1
def prost(a):
    k = 1
    for i in range(2, a):
        if a % i == 0:
            k += 1
    return k == 1


def maxprostdel(a):
    delit = 1
    for i in range(2, a + 1):
        if a % i == 0 and prost(i):
            delit = i
    return delit


# f2

def proizv5(a):
    p = 1
    astr = str(a)
    for i in astr:
        if (int(i) % 5 != 0):
            p *= int(i)
    return p

