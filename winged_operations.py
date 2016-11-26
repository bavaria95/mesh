from helper import *
from point import *
from winged_edge import *

def winged_inc_vertexes(v, edges, vertices, faces):
    level1, level2 = [], []

    for e in v.edges:
        if e.vert1 == v:
            level1.append(e.vert2)
        else:
            level1.append(e.vert1)

    for w in level1:
        for e in w.edges:
            if e.vert1 == w:
                if e.vert2 not in level2 and e.vert2 != v:
                    level2.append(e.vert2)
            else:
                if e.vert1 not in level2 and e.vert1 != v:
                    level2.append(e.vert1)

    return (level1, level2)

def winged_inc_faces(f, edges, vertices, faces):
    level1, level2 = [], []

    for e in f.edges:
        if e.faceA and e.faceA != f:
            level1.append(e.faceA)
        if e.faceB and e.faceB != f:
            level1.append(e.faceB)

    for t in level1:
        for e in t.edges:
            if e.faceA and e.faceA != f and e.faceA not in level2:
                level2.append(e.faceA)
            if e.faceB and e.faceB != f and e.faceB not in level2:
                level2.append(e.faceB)

    return (level1, level2)

def _vertices_of_face(face):
    vx = []
    for e in face.edges:
        if e.vert1 not in vx:
            vx.append(e.vert1)
        if e.vert2 not in vx:
            vx.append(e.vert2)

    return vx

def winged_face_contains_point(face, p, edges, vertices, faces):
    f = face
    path = [f]

    while True:
        vx = _vertices_of_face(f)
        if inside_face(p, *vx):
            return path
        min_dist = 10e8
        min_edge = None
        for e in f.edges:
            p1 = e.vert1
            p2 = e.vert2
            pm = p1 + p2
            d = p.dist(Point(pm.x / 2, pm.y / 2))
            if d < min_dist:
                min_dist = d
                min_edge = e

        e = min_edge
        if e.faceA == f:
            f = e.faceB
        else:
            f = e.faceA
        path.append(f)

def winged_replace_diagonal(f1, f2, edges, vertices, faces):
    e = [val for val in f1.edges if val in f2.edges]
    if len(e) != 1:
        raise Exception("Faces are not incident")
    e = e[0]

    v1 = e.vert1
    v2 = e.vert2

    e1 = e.bPrev
    e2 = e.bNext
    e3 = e.aPrev
    e4 = e.aNext

    if e1.vert1 == v1:
        v3 = e1.vert2
    else:
        v3 = e1.vert1

    if e4.vert1 == v2:
        v4 = e4.vert2
    else:
        v4 = e4.vert1

    v1.edges.remove(e)
    v2.edges.remove(e)

    edges.remove(e)

    faces.remove(f1)
    faces.remove(f2)

    e_new = WE_Edge(v3, v4)
    edges.append(e_new)

    v3.add_edge(e_new)
    v4.add_edge(e_new)

    f3 = WE_Face(e1, e3, e_new)
    f4 = WE_Face(e2, e4, e_new)

    faces.append(f3)
    faces.append(f4)

    e_new.add_face(f3)
    e_new.add_face(f4)
