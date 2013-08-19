'''Jason A Smith'''
def solutionsForPerimeter(perimeter):
    solutions = []
    for a in range(1, perimeter // 2):
        for b in range(a, perimeter // 2):
            c = perimeter - a - b
            if a*a + b*b == c*c:
                solutions.append((a, b, c))
    return solutions

allSolutions = {}
for p in range(12, 1001):
    allSolutions[p] = solutionsForPerimeter(p)

maxSolution = 0
maxNumSolutions = 0
for s in allSolutions:
    if len(allSolutions[s]) > maxNumSolutions:
        maxSolution = s
        maxNumSolutions = len(allSolutions[s])

print(maxSolution)
