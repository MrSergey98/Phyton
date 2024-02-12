import math
import random
import statistics
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




# 2-4

# #3

def randomstring(a):
    q = a.split()
    b = random.sample(range(len(q)), len(q))
    newstr = ""
    for i in b:
        newstr += q[i] + " "
    return newstr

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


# 11-14

def sortstringsbyq():
    a = input("Введие строку, 0 для завершения\n")
    b = []
    while a != "0":
        b.append(a)
        a = input("Введие строку, 0 для завершения\n")
    m = []
    q = {'о':9.28, 'а': 8.66, 'е' : 8.10, 'и' : 7.45, 'н' : 6.35, 'т' : 6.30, 'р' : 5.53, 'с' : 5.45, 'л' : 4.32, 'в' : 4.19,
         'к' : 3.47, 'п' : 3.35, 'м' : 3.29, 'у' : 2.90, 'д' : 2.56, 'я' : 2.22, 'ы' : 2.11, 'ь' : 1.90, 'з' : 1.81, 'б' : 1.51,
         'г' : 1.41, 'й' : 1.31, 'ч' : 1.27, 'ю' : 1.03, 'х' : 0.92, 'ж' : 0.78, 'ш' : 0.77, 'ц' : 0.52, 'щ' : 0.49, 'ф' : 0.40,
         'э' : 0.17, 'ъ' : 0.04}
    for string in b:
        sl = {}
        for char in string:
            if char not in sl:
                sl[char] = 1
            else:
                sl[char] += 1
        m.append(sl)
    n = {}
    l = 0
    for seg in m:
        k = abs(seg[list(seg.keys())[0]]-q[list(seg.keys())[0]])
        for i in list(seg.keys())[1::]:
            if abs(seg[i]-q[i]) > k:
                k = abs(seg[i]-q[i])
        n[l] = k
        l += 1
    mk = list(n.keys())
    mv = list(n.values())

    for i in range(len(mv)):
        for j in range(len(mv) - 1):
            if mv[j + 1] < mv[j]:
                k = mv[j]
                mv[j] = mv[j + 1]
                mv[j + 1] = k
                k = mk[j]
                mk[j] = mk[j + 1]
                mk[j + 1] = k
    rm = []
    for i in mk:
        rm.append(b[i])
    return rm

# #5

def sortstringsbyotkl():
    a = input("Введие строку, 0 для завершения\n")
    b = []
    while a != "0":
        b.append(a)
        a = input("Введие строку, 0 для завершения\n")
    m = []
    q = {'о': 9.28, 'а': 8.66, 'е': 8.10, 'и': 7.45, 'н': 6.35, 'т': 6.30, 'р': 5.53, 'с': 5.45, 'л': 4.32, 'в': 4.19,
         'к': 3.47, 'п': 3.35, 'м': 3.29, 'у': 2.90, 'д': 2.56, 'я': 2.22, 'ы': 2.11, 'ь': 1.90, 'з': 1.81, 'б': 1.51,
         'г': 1.41, 'й': 1.31, 'ч': 1.27, 'ю': 1.03, 'х': 0.92, 'ж': 0.78, 'ш': 0.77, 'ц': 0.52, 'щ': 0.49, 'ф': 0.40,
         'э': 0.17, 'ъ': 0.04}
    for string in b:
        sl = {}
        for char in string:
            if char not in sl:
                sl[char] = 1
            else:
                sl[char] += 1
        m.append(sl)
    n = {}
    l = 0
    for seg in m:
        k = statistics.stdev([seg[list(seg.keys())[0]], q[list(seg.keys())[0]]])
        for i in list(seg.keys())[1::]:
            if statistics.stdev([seg[i], q[i]]) > k:
                k = statistics.stdev([seg[i], q[i]])
        n[l] = k
        l += 1
    mk = list(n.keys())
    mv = list(n.values())

    for i in range(len(mv)):
        for j in range(len(mv) - 1):
            if mv[j + 1] < mv[j]:
                k = mv[j]
                mv[j] = mv[j + 1]
                mv[j + 1] = k
                k = mk[j]
                mk[j] = mk[j + 1]
                mk[j + 1] = k
    rm = []
    for i in mk:
        rm.append(b[i])
    return rm

# #9

def sortstringsbyascii():
    a = input("Введие строку, 0 для завершения\n")
    b = []
    while a != "0":
        b.append(a)
        a = input("Введие строку, 0 для завершения\n")
    n = {}
    l = 0
    for string in b:
        k = 0
        for char in string:
            if ord(char) > k:
                k = ord(char)
        lstr = int(len(string)/2)-1
        dif = 0
        if len(string) % 2 == 0:
            dif = abs(ord(string[lstr])-ord(string[lstr+1]))
        else:
            dif = abs(ord(string[lstr]) - ord(string[lstr + 2]))
        o = math.sqrt(((k-dif)**2)/2)
        n[l] = o
        l += 1
    mk = list(n.keys())
    mv = list(n.values())
    for i in range(len(mv)):
        for j in range(len(mv) - 1):
            if mv[j + 1] < mv[j]:
                k = mv[j]
                mv[j] = mv[j + 1]
                mv[j + 1] = k
                k = mk[j]
                mk[j] = mk[j + 1]
                mk[j + 1] = k
    rm = []
    for i in mk:
        rm.append(b[i])
    return rm

# #11

def sortstringsbyascii2():
    a = input("Введие строку, 0 для завершения\n")
    b = []
    while a != "0":
        b.append(a)
        a = input("Введие строку, 0 для завершения\n")
    n = {}
    max1 = 0
    for i in range(0, len(b[0]), 3):
        c1 = ord(b[0][i])
        c2 = ord(b[0][i])
        c3 = ord(b[0][i])
        if (c1 + c2 + c3) / 3 > max1:
            max1 = (c1 + c2 + c3) / 3
    l = 0
    for string in b:
        max = 0
        for i in range(0, len(string)-3, 3):
            c1 = ord(string[i])
            c2 = ord(string[i+1])
            c3 = ord(string[i+2])
            if (c1+c2+c3)/3 > max:
                max = (c1+c2+c3)/3
        n[l] = ((max-max1)/2)**2
        l += 1
    mk = list(n.keys())
    mv = list(n.values())
    for i in range(len(mv)):
        for j in range(len(mv) - 1):
            if mv[j + 1] < mv[j]:
                k = mv[j]
                mv[j] = mv[j + 1]
                mv[j + 1] = k
                k = mk[j]
                mk[j] = mk[j + 1]
                mk[j + 1] = k
    rm = []
    for i in mk:
        rm.append(b[i])
    return rm

# 15-19

# #9
def elementsprevmin(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    l = 0
    for i in range(len(a)):
        if a[i] == min:
            l = i
    return a[:l]

# #21


def elementsaftermax(a):
    max1 = max(a)
    i = a.index(max1)
    return a[i+1:]

# #33


def proovealternation(a):
    prov = 1
    for i in range(len(a)-1):
        if a[i] > 0 and a[i+1] > 0 or a[i] < 0 and a[i+1] < 0:
            prov = 0
    if prov == 1:
        return True
    return False

# #45


def sumelemininterval(m,a,b):
    sum = 0
    for i in m:
        if a < i < b:
            sum += i
    return sum

# #57


def countelementsmorethenprev(a):
    k = 0
    s = 0
    for i in a:
        if i > s:
            k += 1
        s += i
    return k


if __name__ == '__main__':
    z = int(input("Введите номер задания\n"))
    match z:
        case 1:
            z = int(input("Введите номер функции\n"))
            match z:
                case 1:
                    a = input("Введите число\n")
                    print(maxprostdel(a))
                case 2:
                    print(proizv5(input("Введите число\n")))
                case 3:
                    print(maxnechnepr(input("Введите число\n")))
        case 2:
            print(randomstring(input("Введите троки\n")))
        case 3:
            print(kolsv(input("Введите строку\n")))
        case 4:
            print(flag())
        case 5:
            print(dats(input("Введите текст\n")))
        case 6:
            print(lenrus(input("Введите текст\n")))
        case 7:
            print(leneng(input("Введите текст\n")))
        case 8:
            print(mindigit(input("Введите текст\n")))
        case 9:
            print(sortstringsbychars())
        case 10:
            print(sortstringsbywords())
        case 11:
            print(sortstringsbyq())
        case 12:
            print(sortstringsbyotkl())
        case 13:
            print(sortstringsbyascii())
        case 14:
            print(sortstringsbyascii2())
        case 15:
            a = []
            z = int(input("Введите элемент массива, 0 - признак конца\n"))
            while z != 0:
                a.append(z)
                z = int(input("Введите элемент массива, 0 - признак конца\n"))
            print(elementsprevmin(a))
        case 16:
            a = []
            z = int(input("Введите элемент массива, 0 - признак конца\n"))
            while z != 0:
                a.append(z)
                z = int(input("Введите элемент массива, 0 - признак конца\n"))
            print(elementsaftermax(a))
        case 17:
            a = []
            z = int(input("Введите элемент массива, 0 - признак конца\n"))
            while z != 0:
                a.append(z)
                z = int(input("Введите элемент массива, 0 - признак конца\n"))
            print(proovealternation(a))
        case 18:
            a = []
            z = int(input("Введите элемент массива, 0 - признак конца\n"))
            while z != 0:
                a.append(z)
                z = int(input("Введите элемент массива, 0 - признак конца\n"))
            z1 = int(input("Введите (a\n"))
            z2 = int(input("Введите b)\n"))
            print(sumelemininterval(a, z1, z2))
        case 19:
            a = []
            z = int(input("Введите элемент массива, 0 - признак конца\n"))
            while z != 0:
                a.append(z)
                z = int(input("Введите элемент массива, 0 - признак конца\n"))
            print(countelementsmorethenprev(a))
