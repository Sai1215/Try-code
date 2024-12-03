from functools import reduce

def is_even(num):
    return num % 2 == 0

def append_even(acc, num):
    if is_even(num):
        acc.append(num)
    return acc

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = reduce(append_even, numbers, [])

print(even_numbers)