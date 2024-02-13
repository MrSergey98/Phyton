import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def move(self, x, y):
        self.p1.x += x
        self.p1.y += y
        self.p2.x += x
        self.p2.y += y
        self.p3.x += x
        self.p3.y += y

    def square(self):
        a = math.sqrt((self.p1.x-self.p2.x)**2 + (self.p1.y-self.p2.y)**2)
        b = math.sqrt((self.p2.x-self.p3.x)**2 + (self.p2.y-self.p3.y)**2)
        c = math.sqrt((self.p1.x-self.p3.x)**2 + (self.p1.y-self.p3.y)**2)
        p = (a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))


class Pentagon:

    def __init__(self, p1, p2, p3, p4, p5):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5

    def move(self, x, y):
        self.p1.x += x
        self.p1.y += y
        self.p2.x += x
        self.p2.y += y
        self.p3.x += x
        self.p3.y += y
        self.p4.x += x
        self.p4.y += y
        self.p5.x += x
        self.p5.y += y

    def square(self):
        a = math.sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)
        b = math.sqrt((self.p2.x - self.p3.x) ** 2 + (self.p2.y - self.p3.y) ** 2)
        c = math.sqrt((self.p3.x - self.p4.x) ** 2 + (self.p3.y - self.p4.y) ** 2)
        d = math.sqrt((self.p4.x - self.p5.x) ** 2 + (self.p4.y - self.p5.y) ** 2)
        e = math.sqrt((self.p5.x - self.p1.x) ** 2 + (self.p5.y - self.p1.y) ** 2)
        p = (a+b+c+d+e)/2
        return math.sqrt(p * (p - a) * (p - b) * (p - c) * (p - d) * (p - e))


def compare(t1, t2):
    if t1.square() > t2.square():
        return type(t1)
    else:
        return type(t2)


if __name__ == '__main__':
    print("Inp points for Triangle")
    pt = []
    for i in range(3):
        x = int(input("Inp x\n"))
        y = int(input("Inp y\n"))
        pt.append(Point(x, y))
    tringle = Triangle(pt[0], pt[1], pt[2])
    print("Inp points for Pentagon")
    pp = []
    for i in range(5):
        x = int(input("Inp x\n"))
        y = int(input("Inp y\n"))
        pp.append(Point(x, y))
    pentagon = Pentagon(pp[0], pp[1], pp[2], pp[3], pp[4])
    tringle.move(input("Inp x\n"), input("Inp y\n"))
    pentagon.move(input("Inp x\n"), input("Inp y\n"))
    print(compare(tringle, pentagon))

