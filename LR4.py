import math

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

if __name__ == "__main__":
    a = "C:\\Users\\s0169591\\Desktop\\27-122a.txt"
    b = "C:\\Users\\s0169591\\Desktop\\27-122b.txt"
    commuting(a)
    commuting(b)
