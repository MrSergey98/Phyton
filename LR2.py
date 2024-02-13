

# 1

def poliglots():
    k = int(input("Input k of students\n"))
    n = {}
    for i in range(k):
        kl = int(input("Input k of lang\n"))
        for j in range(kl):
            lang = input("Input lang\n")
            if lang not in n:
                n[lang] = 1
            else:
                n[lang] += 1
    anl = []
    nao = []
    for i in n.keys():
        if n[i] == k:
            anl.append(i)
        nao.append(i)
    anl.sort()
    nao.sort()
    print(len(anl))
    for i in anl:
        print(i)
    print(len(nao))
    for i in nao:
        print(i)

