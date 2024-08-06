def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

# Example usage:
numbers = [3, 1, 4, 1,  5, 9, 2]
median = find_median(numbers)
print(median)