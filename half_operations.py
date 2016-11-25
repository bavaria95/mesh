def _walk_thru(edge, reverse=False):
    e = edge
    visited_faces = []
    f = e.face
    nodes = []

    while f not in visited_faces:
        visited_faces.append(f)
        e = e.next
        if reverse:
            nodes.append(e.prev.origin)
        else:
            nodes.append(e.origin)

        nodes.append(e.next.origin)

        if not reverse:
            e = e.next

        e = e.twin
        if not e:
            break
        f = e.face

    return nodes

def _half_vertex_neighbours(v):
    nodes = []
    e = v.half_edge

    nodes.extend(_walk_thru(e))
    if e.twin:
        nodes.extend(_walk_thru(e.twin, reverse=True))

    nodes = reduce(lambda l, x: l if x in l else l+[x], nodes, [])

    return nodes

def half_inc_vertexes(v, edges, vertices, face):
    level1, level2 = [], []

    level1 = _half_vertex_neighbours(v)

    for w in level1:
        level2.extend(_half_vertex_neighbours(w))

    level2 = reduce(lambda l, x: l if x in l else l+[x], level2, [])
    level2.remove(v)

    return (level1, level2)
