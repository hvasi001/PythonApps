def geometric_series_sum(a, r, n):
    if r == 1:
        return a * n
    else:
        return a * (1 - r**n) / (1 - r)

a = 3
r = 2
n = 5

sum_of_series = geometric_series_sum(a, r, n)
print(sum_of_series)