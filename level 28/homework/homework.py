numbers = list(range(1, 21))  # სია 1-დან 20-მდე
for number in numbers:
    if number % 2 == 0:
        print(f"{number} - ლუწია")
    else:
        print(f"{number} - კენტია")


numbers = list(range(1, 21))  # სია 1-დან 20-მდე
for number in numbers:
    if number % 3 == 0:
        print(number)


numbers = [12, 5, 9, 18, 3, 14, 2, 7, 8, 20, 4, 6, 10, 15, 19, 1, 16, 11, 17, 13]  # 20 სხვადასხვა რიცხვი
for number in numbers:
    if number < 10 and number % 2 == 0:
        print(number)


numbers = [12, 25, 30, 45, 9, 50, 33, 60, 18, 21, 55, 23, 35, 27, 48, 36, 40, 22, 15, 39]  # 20 სხვადასხვა რიცხვი
for number in numbers:
    if number > 20 and number % 3 == 0:
        print(number)


names = ["გიორგი", "ნინო", "მარიამი", "დათო", "სოფიო"]  # ხუთი სახელი
for name in names:
    print(f"{name} - {len(name)} ასო")


names = ["გიორგი", "ნინო", "მარიამი", "დათო", "სოფიო"]  # ხუთი სახელი
for name in names:
    print(f"{name} - {name[0]} პირველი ასო")


family = ["მამა", "დედა", "და", "ძმა"]  # ოჯახის წევრების სახელები
print(family[0])  # მამა
print(family[1])  # დედა
print(family[2])  # და
print(family[3])  # ძმა


numbers = list(range(1, 11))  # სია 1-დან 10-მდე
print(numbers[0])  # პირველი ელემენტი
print(numbers[-1])  # ბოლო ელემენტი


surname = "ჩხეიძე"  # თქვენი გვარი
for letter in surname:
    print(letter)



languages = ["Python", "JavaScript", "Java", "C++", "Ruby"]  # 5 პროგრამირების ენა
print(languages)  # მთლიანი სია
print(languages[-1])  # ბოლო ელემენტი



multiples_of_4 = list(range(0, 21, 4))  # 0-დან 20-მდე 4-ის ჯერადები
print(max(multiples_of_4))  # უდიდესი ელემენტი


odd_numbers = list(range(31, 51, 2))  # 30-დან 50-მდე კენტი რიცხვები
smallest_sum = sum(odd_numbers[:3])  # სამი უმცირესი რიცხვის ჯამი
print(smallest_sum)
