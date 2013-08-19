'''Jason A Smith'''
def triangleGenerator():
    n = 1
    while 1:
        yield (n * (n + 1)) // 2
        n += 1

def pentagonalGenerator():
    n = 1
    while 1:
        yield (n * (3 * n - 1)) // 2
        n += 1

def hexagonalGenerator():
    n = 1
    while 1:
        yield (n * (2 * n - 1))
        n += 1

triangleGen = triangleGenerator()
pentagonalGen = pentagonalGenerator()
hexagonalGen = hexagonalGenerator()

for i in range(285):
    next(triangleGen)

for i in range(165):
    next(pentagonalGen)

for i in range(143):
    next(hexagonalGen)

t = next(triangleGen)
p = next(pentagonalGen)
h = next(hexagonalGen)

while((t != p) or (p != h) or (t != h)):
    smallest = min(t, p, h)
    if smallest == t:
        t = next(triangleGen)
    elif smallest == p:
        p = next(pentagonalGen)
    else:
        h = next(hexagonalGen)

print(t)
