user_input = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))

number = 1

while number <= user_input:
    if number % 5 == 0:
        print(number)
    number += 1