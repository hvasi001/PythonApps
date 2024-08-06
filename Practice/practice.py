def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


print(sum_of_digits(12345))


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print(is_prime(29))
print(is_prime(15))
