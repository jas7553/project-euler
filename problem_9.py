'''Jason A Smith'''
def isPythagoreanTriplet(a, b, c):
    if (a >= b) or (b >= c):
        return False
    return a*a + b*b == c*c

for a in range(1, 998):
    for b in range(a, 998):
        c = 1000 - a - b
        if isPythagoreanTriplet(a, b, c):
            print(a*b*c)
            break
