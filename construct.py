from we import *

def _find_or_create_vertex(x, y, vertices):
    for i in range(len(vertices)):
        if vertices[i].x == x and vertices[i].y == y:
            return vertices[i]

    vertex = WE_Vertex(x, y)
    vertices.append(vertex)

    return vertex

def _find_or_create_edge(vert1, vert2, edges):
    for i in range(len(edges)):
        if (edges[i].vert1 == vert1 and edges[i].vert2 == vert2) or\
           (edges[i].vert1 == vert2 and edges[i].vert2 == vert1):
            return edges[i]

    edge = WE_Edge(vert1, vert2)
    edges.append(edge)

    return edge

def construct_winged_edge(faces_orig):
    edges = []
    vertices = []
    faces = []

    for f in faces_orig:
        vertex0 = _find_or_create_vertex(f[0].x, f[0].y, vertices)
        vertex1 = _find_or_create_vertex(f[1].x, f[1].y, vertices)
        vertex2 = _find_or_create_vertex(f[2].x, f[2].y, vertices)
        
        edge0 = _find_or_create_edge(vertex0, vertex1, edges)
        edge1 = _find_or_create_edge(vertex0, vertex2, edges)
        edge2 = _find_or_create_edge(vertex1, vertex2, edges)

        face = WE_Face(edge0, edge1, edge2)
        faces.append(face)

        if edge0 not in vertex0.edges:
            vertex0.add_edge(edge0)
        if edge1 not in vertex0.edges:
            vertex0.add_edge(edge1)
        if edge0 not in vertex1.edges:
            vertex1.add_edge(edge0)
        if edge2 not in vertex1.edges:
            vertex1.add_edge(edge2)
        if edge1 not in vertex2.edges:
            vertex2.add_edge(edge1)
        if edge2 not in vertex2.edges:
            vertex2.add_edge(edge2)

        edge0.add_face(face)
        edge1.add_face(face)
        edge2.add_face(face)



    for e in edges:
        print(e)
    print
    for v in vertices:
        print(v)
    print
    for f in faces:
        print(f)

    return (edges, vertices, faces)
