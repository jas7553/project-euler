'''Jason A Smith'''
def next(number):    
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

biggestNumber = 0
biggestSequence = 0
results = {}

for i in range(1, 1000000, 2):
    currentSequenceSize = 1
    current = i
    while current != 1:
        current = next(current)
        if current in results:
            currentSequenceSize += results[current]
            break
        currentSequenceSize += 1
    results[i] = currentSequenceSize
    biggestSequence = max(biggestSequence, currentSequenceSize)
    biggestNumber = i if biggestSequence == currentSequenceSize else biggestNumber

print(biggestNumber)
