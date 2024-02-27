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


if __name__ == "__main__":
    # a_file = "C:\\Users\\s0169591\\Desktop\\27-122a.txt"
    # b_file = "C:\\Users\\s0169591\\Desktop\\27-122b.txt"
    # commuting(a_file)
    # commuting(b_file)
    text_file = "text.txt"
    print(find_word(text_file))
