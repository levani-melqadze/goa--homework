
# მომხმარებლისთვის რიცხვების შეყვანა
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

# არითმეტიკული ოპერაციები
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"
modulus = num1 % num2 if num2 != 0 else "Cannot find modulus with zero"
exponentiation = num1 ** num2

# შედეგების დაბეჭვდა
print(f"\n{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {exponentiation}")
