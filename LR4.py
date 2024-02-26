import math


# 1

def cost_commuting(file_path):
    a = open(file_path)
    tmpString = a.readline().split()
    punkts_count = int(tmpString[0])
    kolbs_size = int(tmpString[1])
    punkts_kolbs_sl = {}
    for string in a:
        punkt = int(string.split()[0])
        kolbs = math.ceil(int(string.split()[1])/kolbs_size)
        punkts_kolbs_sl[punkt] = kolbs
    max_punkt = list(punkts_kolbs_sl.keys())[0]
    cost = 0
    for punkt in punkts_kolbs_sl.keys():
        cost += abs(max_punkt - punkt) * punkts_kolbs_sl[punkt]
    for i in list(punkts_kolbs_sl.keys())[1:]:
        loc_cost = 0
        max_punkt = i
        for punkt in punkts_kolbs_sl.keys():
            loc_cost += abs(max_punkt - punkt) * punkts_kolbs_sl[punkt]
        if loc_cost < cost:
            cost = loc_cost
    print(cost)
    a.close()


if __name__ == "__main__":
    a = "27-122a.txt"
    b = "27-122b.txt"
    cost_commuting(a)
    #cost_commuting(b)
