'''Jason A Smith'''
solutions = set()
for a in range(2, 101):
    for b in range(2, 101):
        solutions.add(a**b)

print(len(solutions))
