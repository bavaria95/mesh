class HE_Vertex:
    __i = 0

    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.half_edge = None

        if name:
            self.id = name
        else:
            self.id = HE_Vertex.__i
            HE_Vertex.__i += 1

    def set_half_edge(self, half_edge):
        self.half_edge = half_edge

    def __eq__(self, a):
        return self.x == a.x and self.y == a.y

    def __repr__(self):
        return "VERTEX %s: (%s, %s), %s" % (self.id, self.x, self.y, self.half_edge)


class HE_Half_Edge:
    __i = 0

    def __init__(self, origin, name=None):
        self.origin = origin
        self.face = None
        self.prev = None
        self.next = None

        if name:
            self.id = name
        else:
            self.id = HE_Half_Edge.__i
            HE_Half_Edge.__i += 1

    def set_twin(self, twin):
        self.twin = twin

    def set_face(self, face):
        self.face = face

    def set_prev(self, prev_e):
        self.prev = prev_e

    def set_next(self, next_e):
        self.next = next_e

    def __repr__(self):
        return "EDGE %s, origin=%s, twin=(%s), prev=(%s), next=(%s)" % (self.id, self.origin.id, self.twin.id, self.prev.id if self.prev else None, self.next.id if self.next else None)


class HE_Face:
    __i = 0

    def __init__(self, half_edge, name=None):
        self.half_edge = half_edge

        if name:
            self.id = name
        else:
            self.id = HE_Face.__i
            HE_Face.__i += 1

    def __repr__(self):
        return "FACE %s, half_edge = %s" % (self.id, self.half_edge)

