from winged_edge import *
from half_edge import *
from helper import *

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

def _find_or_create_half_edges(vertA, vertB, half_edges, edges):
    twin = None
    for he in half_edges:
        if (he.edge.vertA == vertA and he.edge.vertB == vertB) or\
           (he.edge.vertA == vertB and he.edge.vertB == vertA):
            twin = he

    edge = HE_Edge(vertA, vertB)
    he = HE_Half_Edge(edge, vertA)
    edge.add_half_edge(he)
    edges.append(edge)

    vertA.set_half_edge(he)

    if twin:
        he.set_twin(twin)
        twin.set_twin(he)

    half_edges.append(he)

    return he

def construct_half_edge(faces_orig):
    edges = []
    half_edges = []
    vertices = []
    faces = []

    for f in faces_orig:
        vertex0 = _find_or_create_vertex_half(f[0].x, f[0].y, vertices)
        vertex1 = _find_or_create_vertex_half(f[1].x, f[1].y, vertices)
        vertex2 = _find_or_create_vertex_half(f[2].x, f[2].y, vertices)

        if orient(vertex0, vertex1, vertex2) == 1:
            vertex0, vertex1 = vertex1, vertex0

        he0 = _find_or_create_half_edges(vertex0, vertex1, half_edges, edges)
        he1 = _find_or_create_half_edges(vertex2, vertex0, half_edges, edges)
        he2 = _find_or_create_half_edges(vertex1, vertex2, half_edges, edges)

        he0.set_prev(he1)
        he0.set_next(he2)

        he1.set_prev(he2)
        he1.set_next(he0)

        he2.set_prev(he0)
        he2.set_next(he1)

        face = HE_Face(he2)
        faces.append(face)

        he0.set_face(face)
        he1.set_face(face)
        he2.set_face(face)


    for e in half_edges:
        print(e)
    print
    for v in vertices:
        print(v)
    print
    for f in faces:
        print(f)

    return (half_edges, vertices, faces)

