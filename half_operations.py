from helper import *
from point import *

def _walk_thru(edge, reverse=False):
    e = edge
    visited_faces = []
    f = e.face
    vertices = []

    while f not in visited_faces:
        visited_faces.append(f)
        e = e.next
        if reverse:
            vertices.append(e.prev.origin)
        else:
            vertices.append(e.origin)

        vertices.append(e.next.origin)

        if not reverse:
            e = e.next

        e = e.twin
        if not e:
            break
        f = e.face

    return vertices

def _half_vertex_neighbours(v):
    vertices = []
    e = v.half_edge

    vertices.extend(_walk_thru(e))
    if e.twin:
        vertices.extend(_walk_thru(e.twin, reverse=True))

    vertices = reduce(lambda l, x: l if x in l else l+[x], vertices, [])

    return vertices

def half_inc_vertexes(v, edges, vertices, faces):
    level1, level2 = [], []

    level1 = _half_vertex_neighbours(v)

    for w in level1:
        level2.extend(_half_vertex_neighbours(w))

    level2 = reduce(lambda l, x: l if x in l else l+[x], level2, [])
    if v in level2:
        level2.remove(v)

    return (level1, level2)

def _half_face_neighbours(f):
    faces = []
    e = f.half_edge

    for i in range(3):
        if e.twin:
            faces.append(e.twin.face)
        e = e.next

    return faces

def half_inc_faces(face, edges, vertices, faces):
    level1, level2 = [], []

    level1.extend(_half_face_neighbours(face))

    for f in level1:
        level2.extend(_half_face_neighbours(f))

    level2 = reduce(lambda l, x: l if x in l else l+[x], level2, [])
    if face in level2:
        level2.remove(face)

    return (level1, level2)

def _edges_of_face(face):
    edges = []
    e = face.half_edge

    for i in range(3):
        edges.append(e)
        e = e.next

    return edges

def half_face_contains_point(face, p, edges, vertices, faces):
    f = face

    while True:
        vx = [x.origin for x in _edges_of_face(f)]
        if inside_face(p, *vx):
            return f
        min_dist = 10e8
        min_edge = None
        for e in _edges_of_face(f):
            p1 = e.origin
            p2 = e.next.origin
            pm = p1 + p2
            d = p.dist(Point(pm.x / 2, pm.y / 2))
            if d < min_dist:
                min_dist = d
                min_edge = e

        e = min_edge.twin
        f = e.face
