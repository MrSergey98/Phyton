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

# 5

def dats(a):
    tempa = a.split()
    months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля",
              "августа", "сентября", "октября", "ноября", "декабря"]
    d = []
    for i in range(len(tempa) - 2):
        if tempa[i].isdigit() and tempa[i + 2].isdigit():
            if (1 <= int(tempa[i]) and 31 >= int(tempa[i]) and tempa[i + 1] in months and 1 <= int(
                    tempa[i + 2]) and 2025 >= int(tempa[i + 2])):
                d.append(tempa[i] + " " + tempa[i + 1] + " " + tempa[i + 2])
    return d

# 6-8

# #3

def lenrus(a):
    k = 0
    for i in a:
        if "а" <= i.lower() and "я" >= i.lower():
            k += 1
    return k

# #8

def leneng(a):
    k = 0
    for i in a:
        if "a" <= i and "z" >= i:
            k += 1
    return k

# #16

def mindigit(a):
    min = None
    for i in range(len(a)):
        if a[i].isdigit():
            min = int(a[i])
            k = i + 1
            if k == len(a):
                break
            while a[k].isdigit():
                min = int(str(min) + a[k])
                k += 1
                if k == len(a):
                    break
            break

    i = 0

    while i < len(a):
        ch = ""
        if a[i].isdigit():
            ch = a[i]
            k = i + 1
            if k >= len(a):
                if int(a[i]) < min:
                    min = int(a[i])
                break
            while a[k].isdigit():
                ch += a[k]
                k += 1
                if k >= len(a):
                    break
            if int(ch) < min:
                min = int(ch)
            i = k + 1
        else:
            i += 1

    return min

# 9

def sortstringsbychars():
    a = input("Введие строку, 0 для завершения\n")
    b = []
    while a != "0":
        b.append(a)
        a = input("Введие строку, 0 для завершения\n")
    for i in range(len(b)):
        for j in range(len(b) - 1):
            if len(b[j + 1]) > len(b[j]):
                k = b[j]
                b[j] = b[j + 1]
                b[j + 1] = k

    return b

# 10

def sortstringsbywords():
    a = input("Введие строку, 0 для завершения\n")
    b = []
    while a != "0":
        b.append(a)
        a = input("Введие строку, 0 для завершения\n")
    for i in range(len(b)):
        for j in range(len(b) - 1):
            if len(b[j + 1].split()) > len(b[j].split()):
                k = b[j]
                b[j] = b[j + 1]
                b[j + 1] = k
    return b


