'''Jason A Smith'''
def isAllOddDigits(number):
    while number != 0:
        if number % 2 == 0:
            return False
        number //= 10
    return True

def isReversible(number):
    if number % 10 == 0:
        return False
    return isAllOddDigits(number + int(str(number)[::-1]))

count = 0
for i in range(1, 100000000):
    if isReversible(i):
        count += 1

print(count)
