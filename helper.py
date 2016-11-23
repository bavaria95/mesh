def orient(p, q, r):
    orientation = (q.x - p.x) * (r.y - p.y) - (r.x - p.x) * (q.y - p.y)
    if orientation >= 0:
        return 1
    return -1
