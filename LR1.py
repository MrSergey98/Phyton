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

# f3

def maxnechnepr(a):
    delit = 1
    for i in range(2, a + 1):
        if a % 2 != 0 and a % i == 0 and not prost(i):
            delit = i
    return delit

def proizv(a):
    p = 1
    astr = str(a)
    for i in astr:
        p *= int(i)
    return p

def nod(a, b):
    delit = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            delit = i
    return delit

# #3

def randomstring(a):
    q = a.split()
    b = random.sample(range(len(q)), len(q))
    newstr = ""
    for i in b:
        newstr += q[i] + " "
    print(newstr)


# 2-4


# #8


def kolsv(a):
    q = a.split()
    k = 0
    for i in q:
        if len(a) % 2 == 0:
            k += 1
    return k

# #16

def flag():
    a = ["красный", "синий", "белый"]
    random.shuffle(a)
    for i in range(len(a) - 1):
        for j in range(len(a)):
            if (i == 0 and a[j] == "белый") or (i == 1 and a[j] == "синий"):
                k = a[i]
                a[i] = a[j]
                a[j] = k
    return a



