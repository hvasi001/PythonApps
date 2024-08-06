def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
print(sum_of_digits(1234))
print(sum_of_digits(56789))