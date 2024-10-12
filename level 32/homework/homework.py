#შექმენით რიცხვებით სავსე სია, შემდეგ დაწერეთ კოდი რომელიც დაბეჭდავს ამ სიიდან ყველაზე უდიდეს რიცხვს გამოგადგებათ for loop ი კარგად დაფიქრდით და გაიაზრეთ

# რიცხვების სია
numbers = [34, 78, 12, 89, 56, 23, 99, 65]


max_number = numbers[0]


for number in numbers:
    if number > max_number:
        max_number = number

print("სიიდან ყველაზე დიდი რიცხვი არის:", max_number)
