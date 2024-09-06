
correct_password = "your_password_here"  # Replace with the actual password

user_input = ""  # Initialize user_input to enter the loop
while user_input != correct_password:
    user_input = input("გთხოვთ შეიყვანეთ პაროლი!: ")
    if user_input == correct_password:
        print("პაროლი სწორია!")
    else:
        print("პაროლი არასწორია, სცადეთ ხელახლა.")
