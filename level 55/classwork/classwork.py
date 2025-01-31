# 1. ლუწი რიცხვები
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 2. 4 ან მეტი სიმბოლოს მქონე სიტყვები
words = ["cat", "house", "tree", "car"]
long_words = list(filter(lambda w: len(w) >= 4, words))
print(long_words)

# 3. სამის ჯერადი რიცხვები
nums = [3, 9, 15, 22, 27, 30]
multiples_of_three = list(filter(lambda x: x % 3 == 0, nums))
print(multiples_of_three)
