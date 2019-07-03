


# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2 or (m1 < m2 and y1 == y2) or (d1 <= d2 and m1 == m2 and y1 == y2):
        return 0
    elif d1 > d2 and m1 == m2 and y1 == y2:
        return (d1 - d2) * 15
    elif m1 > m2 and y1 == y2:
        return (m1 - m2) * 500
    else:
        return 10000


d1 = 9
d2 = 7
m1 = 4
m2 = 4
y1 = 5
y2 = y1

print(libraryFine(d1, m1, y1, d2, m2, y2))
