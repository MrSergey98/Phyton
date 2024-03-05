import math


# 1

def commuting(path_file):
    file = open(path_file)
    tmpString = file.readline().split()
    kolbs = int(tmpString[1])
    punkts_kolbs = []
    for string in file:
        tmpString = string.split()
        punkts_kolbs.append((int(tmpString[0]), math.ceil(int(tmpString[1])/kolbs)))
    punkts_kolbs.sort()

    costs = []
    left = 0
    right = 0
    cost_first = 0
    for punkt in punkts_kolbs:
        cost_first += abs(punkts_kolbs[0][0]-punkt[0])*punkt[1]
        right += punkt[1]
    costs.append(cost_first)
    for i in range(1, len(punkts_kolbs[1:])):
        left += punkts_kolbs[i-1][1]
        costs.append(costs[-1]-right*(punkts_kolbs[i][0]-punkts_kolbs[i-1][0])+left*(punkts_kolbs[i][0]-punkts_kolbs[i-1][0]))
        right -= punkts_kolbs[i][1]
    print(min(costs))


# 2

def find_word(path_file):
    file = open(path_file, encoding="UTF-16")
    strings = []
    for string in file:
        strings.append(string[:-1])
    literalls = []
    literall = input("Введите букву, 0 - признак конца\n")
    literalls.append(literall)
    while literall != '0':
        literall = input("Введите букву, 0 - признак конца\n")
        literalls.append(literall)
    ret_word = 'й'
    sum_literalls = 0
    for string in strings:
        for word in string.split():
            tmp_sum_literalls = 0
            for lit in literalls:
                tmp_sum_literalls += word.count(lit)
            if tmp_sum_literalls > sum_literalls:
                ret_word = word
                sum_literalls = tmp_sum_literalls
    return ret_word

# 3*


def instabram(path_file):
    file = open(path_file)
    n, k = file.readline().split()
    n = int(n)
    k = int(k)
    string_mas = file.readline()
    massive = []
    mas_sum = 0
    for elem in string_mas.split():
        massive.append(int(elem))
        mas_sum += int(elem)
    if mas_sum % k != 0:
        print("Нет")
    else:
        massive_ind = [0 for i in range(k)]
        loc_sum = 0
        for i in range(len(massive)):
            loc_sum += massive[i]
            if loc_sum > mas_sum/k:
                print("Нет")
                return
            elif loc_sum == mas_sum/k:
                massive_ind[0] = i+1
                break
        for i in range(1, k):
            loc_sum = 0
            for j in range(massive_ind[i-1], len(massive)):
                loc_sum += massive[j]
                if loc_sum > mas_sum / k:
                    print("Нет")
                    return
                elif loc_sum == mas_sum / k:
                    massive_ind[i] = j + 1
                    break
        ret_string = ""+str(massive_ind[0])
        for i in range(1, k):
            ret_string += f" {massive_ind[i]-massive_ind[i-1]}"
        print("Да")
        print(ret_string)


if __name__ == "__main__":
    # 1

    # a_file = "C:\\Users\\s0169591\\Desktop\\27-122a.txt"
    # b_file = "C:\\Users\\s0169591\\Desktop\\27-122b.txt"
    # commuting(a_file)
    # commuting(b_file)

    # 2

    # text_file = "text.txt"
    # print(find_word(text_file))

    # 3*

    file_3 = "3.txt"
    instabram(file_3)
