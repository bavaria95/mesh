class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    def x(self):
        return self.x

    def y(self):
        return self.y

    def __eq__(self, a):
        return self.x == a.x and self.y == a.y

    def __sub__(self, a):
        return Point(self.x - a.x, self.y - a.y)
