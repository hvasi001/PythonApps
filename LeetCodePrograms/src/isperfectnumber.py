def is_perfect_number(n):
    if n < 2:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

print(is_perfect_number(28))
print(is_perfect_number(12))

    