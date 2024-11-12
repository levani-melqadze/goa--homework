def sum_of_two_numbers():
    num1 = float(input("შეიყვანე პირველი რიცხვი: "))
    num2 = float(input("შეიყვანე მეორე რიცხვი: "))
    print("ჯამი:", num1 + num2)

sum_of_two_numbers()
def square_of_number():
    num = float(input("შეიყვანე რიცხვი: "))
    print("რიცხვის კვადრატი არის:", num ** 2)

def name_length():
    name = input("შეიყვანე სახელი: ")
    print(f"შენი სახელის სიმბოლოების რაოდენობა: {len(name)}")

def larger_number():
    num1 = float(input("შეიყვანე პირველი რიცხვი: "))
    num2 = float(input("შეიყვანე მეორე რიცხვი: "))
    if num1 > num2:
        print(f"უფრო დიდი {num1} რიცხვია.")
    elif num2 > num1:
        print(f"უფრო დიდი {num2} რიცხვია.")
    else:
        print("ორივე რიცხვი ტოლია.")

def check_number():
    num = int(input("შეიყვანე რიცხვი: "))
    if 1 <= num <= 10:
        print("რიცხვი 1-დან 10-მდეა")
    else:
        print("არასწორი რიცხვი")

def celsius_to_fahrenheit():
    celsius = float(input("შეიყვანე ტემპერატურა ცელსიუსში: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"ტემპერატურა ფარენჰეიტში: {fahrenheit}")

def text_length():
    text = input("შეიყვანე ტექსტი: ")
    return len(text)


# square_of_number()
# check_number()
# celsius_to_fahrenheit()
# print("ტექსტის სიგრძე:", text_length())

