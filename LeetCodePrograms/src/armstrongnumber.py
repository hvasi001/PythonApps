def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n


print(is_armstrong_number(153))
print(is_armstrong_number(123))
