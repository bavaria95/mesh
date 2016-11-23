class WE_Edge:
    __i = 0

    def __init__(self, vert1, vert2, faceA, faceB, aPrev, aNext, bPrev, bNext, name=None):
        self.vert1 = vert1
        self.vert2 = vert2
        self.faceA = faceA
        self.faceB = faceB
        self.aPrev = aPrev
        self.aNext = aNext
        self.bPrev = bPrev
        self.bNext = bNext

        if name:
            self.id = name
        else:
            self.id = WE_Edge.__i
            WE_Edge.__i += 1

class WE_Vertex:
    __i = 0

    def __init__(self, x, y, edges=[], name=None):
        self.x = x
        self.y = y
        self.edges = edges

        if name:
            self.id = name
        else:
            self.id = WE_Vertex.__i
            WE_Vertex.__i += 1

    def add_edge(self, edge):
        self.edges.append(edge)

class WE_Face:
    __i = 0

    def __init__(self, edge1, edge2, edge3, name=None):
        self.edges = [edge1, edge2, edge3]

        if name:
            self.id = name
        else:
            self.id = WE_Face.__i
            WE_Face.__i += 1

