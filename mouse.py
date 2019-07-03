def mouse(x,y,z):
    f = abs(z - x)
    s = abs(z - y)
    if f > s:
        return "CAT B"
    elif s > f:
        return "CAT A"
    else:
        return "MOUSE C"

print(mouse(1,3,2))