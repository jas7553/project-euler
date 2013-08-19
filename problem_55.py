'''Jason A Smith'''
def isPalandrome(number):
    number = str(number)
    return number == number[::-1]

def isLychrelNumber(number):
    return isLychrelNumberHelper(number, 0)

def isLychrelNumberHelper(number, count):
    if count != 0 and isPalandrome(number):
        return False

    if count >= 50:
        return True
    
    reverse = int(str(number)[::-1])
    return isLychrelNumberHelper(number + reverse, count + 1)

print(sum(1 for i in range(0, 10000) if isLychrelNumber(i)))
