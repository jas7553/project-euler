'''Jason A Smith'''
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print(sum([int(i) for i in str(factorial(100))]))
