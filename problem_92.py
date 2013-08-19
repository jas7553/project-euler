'''Jason A Smith'''
def numberChainGenerator(number):
    current = number
    while 1:
        current = sum([int(i)**2 for i in str(current)])
        yield current

count = 0
seen = {}
for i in range(2, 10000000):
    gen = numberChainGenerator(i)

    temp = []
    arrive = i
    while 1:
        try:
            if seen[arrive] == 89:
                count += 1
                for f in temp:
                    seen[f] = 89
                break
            elif seen[arrive] == 1:
                for f in temp:
                    seen[f] = 1
                break
        except KeyError:
            pass
        
        arrive = next(gen)
        temp.append(arrive)

        if arrive == 89:
            count += 1
            for f in temp:
                seen[f] = 89
            break
        elif arrive == 1:
            for f in temp:
                seen[f] = 1
            break

print(count)
