def orient(p, q, r):
    orientation = (q.x - p.x) * (r.y - p.y) - (r.x - p.x) * (q.y - p.y)
    if orientation >= 0:
        return 1
    return -1

def inside_face(p, a, b, c):
    x, y = p.x, p.y
    xp, yp = zip(*[(q.x, q.y) for q in [a, b, c]])
    c = 0
    for i in range(3):
        if (((yp[i]<=y and y<yp[i-1]) or (yp[i-1]<=y and y<yp[i])) and \
           (x > (xp[i-1] - xp[i]) * (y - yp[i]) / (yp[i-1] - yp[i]) + xp[i])):
            c = 1 - c    

    return c
