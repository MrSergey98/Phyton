import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, p2):
        return math.sqrt((p2.x-self.x)**2+(p2.y-self.y)**2)


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
        sq = Geron(self.p1.distanceTo(self.p2), self.p2.distanceTo(self.p3), self.p1.distanceTo(self.p3))+Geron(self.p1.distanceTo(self.p3), self.p3.distanceTo(self.p4), self.p1.distanceTo(self.p4))+Geron(self.p1.distanceTo(self.p4),self.p4.distanceTo(self.p5), self.p1.distanceTo(self.p5))
        print("Pentagon square: ", sq)
        return sq


def compare(t1, t2):
    if t1.square() > t2.square():
        return type(t1)
    else:
        return type(t2)


def Geron(a, b, c):
    p=(a+b+c)/2
    sq = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(sq)
    return sq


if __name__ == '__main__':
    try:
        print("Inp points for Triangle")
        pt = []
        for i in range(3):
            x = float(input("Inp x\n"))
            y = float(input("Inp y\n"))
            pt.append(Point(x, y))
        tringle = Triangle(pt[0], pt[1], pt[2])
        print("Inp points for Pentagon")
        pp = []
        for i in range(5):
            x = float(input("Inp x\n"))
            y = float(input("Inp y\n"))
            pp.append(Point(x, y))
        pentagon = Pentagon(pp[0], pp[1], pp[2], pp[3], pp[4])
        #tringle.move(input("Inp x\n"), input("Inp y\n"))
        #pentagon.move(input("Inp x\n"), input("Inp y\n"))
        print(compare(tringle, pentagon))
    except ValueError:
        print("Введено не число!")

