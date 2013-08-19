'''Jason A Smith'''
smaller = 1
bigger = 2
values = []
while bigger < 4000000:
    if bigger % 2 == 0:
        values.append(bigger)
    smaller, bigger = bigger, smaller + bigger

print(sum(values))
