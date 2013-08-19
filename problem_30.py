'''Jason A Smith'''
def is_sum_of_fifth_powers_of_its_digits(number):
    return number == sum([int(i)**5 for i in list(str(number))])

solutions = []
for i in range(2, 200000):
    if is_sum_of_fifth_powers_of_its_digits(i):
        solutions.append(i)

print(sum(solutions))
