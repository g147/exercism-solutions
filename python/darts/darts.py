from math import sqrt
def score(x, y):
    inner, middle, outer = 1, 5, 10
    dart = sqrt(x**2+ y**2)
    if dart <= inner:
        return 10
    if dart <= middle:
        return 5
    if dart <= outer:
        return 1
    return 0
