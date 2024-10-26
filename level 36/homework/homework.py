def sum_two_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def is_positive(number):
    return number > 0

def count_elements(lst):
    return len(lst)

def min_of_two(a, b):
    return min(a, b)

def square_numbers(lst):
    return [x**2 for x in lst]

def concatenate_strings(str1, str2):
    return str1 + str2

result_sum = sum_two_numbers(5, 10)
print(result_sum)

even_check = is_even(4)
print(even_check)

positive_check = is_positive(-3)
print(positive_check)

count = count_elements([1, 2, 3, 4])
print(count)

minimum = min_of_two(7, 2)
print(minimum)

squared = square_numbers([1, 2, 3],)
print(squared)

concatenation = concatenate_strings("Hello, ", "World!")
print(concatenation)
