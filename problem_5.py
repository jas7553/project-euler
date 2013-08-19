'''Jason A Smith'''
def divisibleByAllNumbersFromOneToTwenty(number):
    for i in [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]:
        if not(number % i == 0):
            return False
    return True

number = 20
while not divisibleByAllNumbersFromOneToTwenty(number):
    number += 20

print(number)
