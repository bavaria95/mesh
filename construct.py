from winged_edge import *
from half_edge import *

def _find_or_create_vertex_winged(x, y, vertices):
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
        vertex0 = _find_or_create_vertex_winged(f[0].x, f[0].y, vertices)
        vertex1 = _find_or_create_vertex_winged(f[1].x, f[1].y, vertices)
        vertex2 = _find_or_create_vertex_winged(f[2].x, f[2].y, vertices)
        
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



def _find_or_create_vertex_half(x, y, vertices):
    for i in range(len(vertices)):
        if vertices[i].x == x and vertices[i].y == y:
            return vertices[i]

    vertex = HE_Vertex(x, y)
    vertices.append(vertex)

    return vertex 

def _find_or_create_half_edges(vertA, vertB, half_edges):
    for he in half_edges:
        if he.origin == vertA and he.next and he.next.origin == vertB or\
           he.origin == vertB and he.next and he.next.origin == vertA:
            print(he, he.twin)
            return (he, he.twin)

    heA = HE_Half_Edge(vertA)
    heB = HE_Half_Edge(vertB)
    heA.set_twin(heB)
    heB.set_twin(heA)

    half_edges.append(heA)
    half_edges.append(heB)

    return (heA, heB)

def construct_half_edge(faces_orig):
    half_edges = []
    vertices = []
    faces = []

    for f in faces_orig:
        vertex0 = _find_or_create_vertex_half(f[0].x, f[0].y, vertices)
        vertex1 = _find_or_create_vertex_half(f[1].x, f[1].y, vertices)
        vertex2 = _find_or_create_vertex_half(f[2].x, f[2].y, vertices)

        he01, he02 = _find_or_create_half_edges(vertex0, vertex1, half_edges)
        he11, he12 = _find_or_create_half_edges(vertex2, vertex0, half_edges)
        he21, he22 = _find_or_create_half_edges(vertex1, vertex2, half_edges)


        he01.set_prev(he11)
        he01.set_next(he21)

        he11.set_prev(he21)
        he11.set_next(he01)

        he21.set_prev(he01)
        he21.set_next(he11)

        he02.set_prev(he22)
        he02.set_next(he12)

        he12.set_prev(he02)
        he12.set_next(he22)

        he22.set_prev(he12)
        he22.set_next(he02)

        face = HE_Face(he02)
        faces.append(face)


    for e in half_edges:
        print(e)
    print
    for v in vertices:
        print(v)
    print
    for f in faces:
        print(f)

    return (half_edges, vertices, faces)

