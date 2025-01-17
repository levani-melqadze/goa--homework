# 2) ცვლადი, რომელიც აბრუნებს 2 სტრინგის ჯამს
concat_strings = lambda s1, s2: s1 + s2

# 3) ცვლადი, რომელიც აბრუნებს 3 რიცხვის ჯამს
sum_three_numbers = lambda a, b, c: a + b + c

# 4) ცვლადი, რომელიც იღებს list-ს და აბრუნებს მასში მყოფი რიცხვების ჯამს
sum_list = lambda lst: sum(lst)

# 5) ცვლადი, რომელიც იღებს string-ს და სიმბოლოს და აბრუნებს რამდენჯერ მეორდება სიმბოლო string-ში
count_symbol = lambda string, symbol: string.count(symbol)
# 2)
print(concat_strings("გამარჯობა", " მსოფლიო"))  # შედეგი: "გამარჯობა მსოფლიო"

# 3)
print(sum_three_numbers(10, 20, 30))  # შედეგი: 60

# 4)
print(sum_list([1, 2, 3, 4, 5]))  # შედეგი: 15

# 5)
print(count_symbol("banana", "a"))  # შედეგი: 3
