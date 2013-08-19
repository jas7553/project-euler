'''Jason A Smith'''
def isPalandrome(number):
    if len(number) == 0 or len(number) == 1:
        return True
    else:
        if number[0] == number[-1]:
            return isPalandrome(number[1:-1])
        else:
            return False

sum = 0

for i in range(1, 1000000, 2):
    base10 = str(i)
    base2 = bin(i)[2:]
    if isPalandrome(base10) and isPalandrome(base2):
        sum += i

print(sum)
