# Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
