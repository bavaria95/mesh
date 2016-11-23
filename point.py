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
