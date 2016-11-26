from helper import *
from point import *
from half_edge import *

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
    level2 = filter(lambda p: p not in level1, level2)

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
    path = [f]

    while True:
        vx = [x.origin for x in _edges_of_face(f)]
        if inside_face(p, *vx):
            return path
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
        path.append(f)

def half_replace_diagonal(f1, f2, edges, vertices, faces):
    f1_edges = _edges_of_face(f1)
    f2_edges = _edges_of_face(f2)

    e = [val for val in f1_edges if val in [e.twin for e in f2_edges]]
    if len(e) != 1:
        raise Exception("Faces are not incident")
    e = e[0]

    v1 = e.twin.origin
    v2 = e.origin

    v3 = e.prev.origin
    v4 = e.twin.prev.origin

    new_full_edge = HE_Edge(v3, v4)

    e_new = HE_Half_Edge(new_full_edge, v3)
    e_new_twin = HE_Half_Edge(new_full_edge, v4)

    new_full_edge.add_half_edge(e_new)
    new_full_edge.add_half_edge(e_new_twin)

    e_new.set_twin(e_new_twin)
    e_new_twin.set_twin(e_new)

    e_new.set_prev(e.next)
    e_new.set_next(e.twin.prev)
    e_new_twin.set_prev(e.twin.next)
    e_new_twin.set_next(e.prev)

    e.next.set_prev(e.twin.prev)
    e.next.set_next(e_new)
    e.twin.prev.set_prev(e_new)
    e.twin.prev.set_next(e.next)
    e.prev.set_prev(e_new_twin)
    e.prev.set_next(e.twin.next)
    e.twin.next.set_prev(e.prev)
    e.twin.next.set_next(e_new_twin)


    f3 = HE_Face(e_new)
    f4 = HE_Face(e_new_twin)

    e_new.set_face(f3)
    e_new.next.set_face(f3)
    e_new.next.next.set_face(f3)

    e_new_twin.set_face(f4)
    e_new_twin.next.set_face(f4)
    e_new_twin.next.next.set_face(f4)

    v1.set_half_edge(e_new.prev)
    v2.set_half_edge(e_new_twin.prev)
    v3.set_half_edge(e_new)
    v4.set_half_edge(e_new_twin)

    edges.remove(e)
    edges.remove(e.twin)
    edges.append(e_new)
    edges.append(e_new_twin)

    faces.remove(f1)
    faces.remove(f2)
    faces.append(f3)
    faces.append(f4)
