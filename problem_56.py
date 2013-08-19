'''Jason A Smith'''
def digitalSum(number):
    return sum([int(i) for i in list(str(number))])

solution = 1
for a in range(1, 100):
    for b in range(1, 100):
        solution = max(solution, digitalSum(a**b))

print(solution)
