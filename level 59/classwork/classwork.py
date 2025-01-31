numbers = [10, 25, 40, 55, 70, 15, 90]

filtered_numbers = list(filter(lambda x: x >= 40, numbers))

print(filtered_numbers)

numbers = [2, 4, 6, 8, 10]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)



words = ["banana", "apple", "mango", "papaya", "cherry", "guava"]

filtered_words = list(filter(lambda x: x.endswith("a"), words))

print(filtered_words)

