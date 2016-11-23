class WE_Edge:
    __i = 0

    def __init__(self, vert1, vert2, name=None):
        self.vert1 = vert1
        self.vert2 = vert2
        self.faces = []
        self.aPrev = None
        self.aNext = None
        self.bPrev = None
        self.bNext = None

        if name:
            self.id = name
        else:
            self.id = WE_Edge.__i
            WE_Edge.__i += 1

    def add_face(self, face):
        self.faces.append(face)

    def __eq__(self, e):
        return (self.vert1 == e.vert1 and self.vert2 == e.vert2) or \
               (self.vert1 == e.vert2 and self.vert2 == e.vert1)

    def __repr__(self):
        return "EDGE %s: from %s to %s, %s faces." %\
               (self.id, self.vert1.id, self.vert2.id, len(self.faces))

class WE_Vertex:
    __i = 0

    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.edges = []

        if name:
            self.id = name
        else:
            self.id = WE_Vertex.__i
            WE_Vertex.__i += 1

    def add_edge(self, edge):
        self.edges.append(edge)

    def __eq__(self, a):
        return (self.x == a.x and self.y == a.y)

    def __repr__(self):
        return "VERTEX %s: (%s, %s), %s" % (self.id, self.x, self.y, [x.id for x in self.edges])

class WE_Face:
    __i = 0

    def __init__(self, edge1, edge2, edge3, name=None):
        self.edges = [edge1, edge2, edge3]

        if name:
            self.id = name
        else:
            self.id = WE_Face.__i
            WE_Face.__i += 1

    def __repr__(self):
        return "FACE %s: %s" % (self.id, [x.id for x in self.edges])

