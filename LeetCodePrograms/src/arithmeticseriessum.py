def arithmetic_series_sum(a, d, n):
    return (n/2) * (2 * a + (n - 1) * d)

a = 2
d = 3
n = 5

sum_of_series = arithmetic_series_sum(a, d, n)
print(sum_of_series)