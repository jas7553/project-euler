'''Jason A Smith'''
sumList = []
newSumList = []

triangle = [[int(i) for i in line.split()] for line in open('problem_18.txt')]
sumList.append(triangle.pop(0)[0])

for row in triangle:
    print(sumList)
    print(row)
    print()
    i = 0
    for i in range(len(sumList)):
        newSumList.append(sumList[i] + row[i])
        newSumList.append(sumList[i] + row[i+1])
    sumList = newSumList
    newSumList = []

print(sumList)
sumList.sort()
print(sumList[-1])
