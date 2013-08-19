'''Jason A Smith'''
digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def numLettersInNumber(number):
    if number in range(0, 10):
        return len(digits[number])
    
    elif number in range(10, 20):
        return len(teens[number - 10])
    
    elif number in range(20, 100):
        return len(tens[number // 10 - 2]) + len(digits[number % 10])
    
    elif number in range(100, 1000):
        if number % 100 == 0:
            return len(digits[number // 100]) + len('hundred')
        else:
            return len(digits[number // 100]) + len('hundred') + len('and') + numLettersInNumber(number % 100)

resultSum = sum([numLettersInNumber(i) for i in range(1, 1000)]) + len('onethousand')

print(resultSum)
