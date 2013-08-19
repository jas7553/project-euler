'''Jason A Smith'''
allPowers = [[] for i in range(0, 30)]

for i in range(0, 30):
    base = 1
    allNPowers = []
    while 1:
        number = base ** i
        if len(str(number)) < i:
            pass
        elif len(str(number)) == i:
            allNPowers.append(number)
        elif len(str(number)) > i:
            break
        base += 1
    allPowers[i] = allNPowers

for i in allPowers:
    print(i)

print(sum([len(i) for i in allPowers]))
