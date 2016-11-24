import numpy as np
import matplotlib.pyplot as plt
from point import *
from construct import *
from winged_operations import *

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
    minx, maxx = min(x), max(x)
    miny, maxy = min(y), max(y)
    # plt.plot(x, y, 'o')

    # for f in faces:
    #     x = [p.x for p in f]
    #     x += [x[0]]
    #     y = [p.y for p in f]
    #     y += [y[0]]
    #     plt.plot(x, y, 'r-')

    # axes = plt.gca()
    # axes.set_xlim([minx-0.5, maxx+0.5])
    # axes.set_ylim([miny-0.5, maxy+0.5])

    # plt.show()
    
    w_edges, w_vertices, w_faces = construct_winged_edge(faces)
    print('-'*80)
    h_edges, h_vertices, h_faces = construct_half_edge(faces)
    print('-'*80)

    v = w_vertices[0]
    lvl1_v, lvl2_v = winged_inc_vertexes(v, w_edges, w_vertices, w_faces)

    f = w_faces[0]
    lvl1_f = winged_inc_faces(f, w_edges, w_vertices, w_faces)

    p = Point(5.0, 4.0)
