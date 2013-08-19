'''Jason A Smith'''
solution_numerator = 1
solution_denominator = 1

for n in range(11, 100):
    for d in range(11, 100):
        div = n / d
        n_tens = n // 10
        n_ones = n % 10
        d_tens = d // 10
        d_ones = d % 10
        if n % 11 == 0 and d % 11 == 0:
            continue
        if n_ones == d_tens and d_ones != 0:
            curious_div = n_tens / d_ones
            if curious_div == div:
                print('n: ' + str(n) + ' d: ' +str(d))
                solution_numerator *= n
                solution_denominator *= d

print(solution_numerator)
print(solution_denominator)
