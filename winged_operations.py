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

def winged_cont_point(f, p, edges, vertices, faces):
    pass
