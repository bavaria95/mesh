import numpy as np
import matplotlib.pyplot as plt
from point import *


if __name__ == "__main__":
    filename = 'data.dat'
    points = []
    faces = []

    for l in open(filename).readlines():
        w = l.split()
        if len(w) == 2:
            points.append(Point(float(w[0]), float(w[1])))
        if len(w) == 3:
            n1, n2, n3 = map(int, w)
            faces.append((points[n1], points[n2], points[n3]))

    x = [p.x for p in points]
    y = [p.y for p in points]
    plt.plot(x, y, 'o')

    for f in faces:
        x = [p.x for p in f]
        x += [x[0]]
        y = [p.y for p in f]
        y += [y[0]]
        plt.plot(x, y, 'r-')

    plt.show()
