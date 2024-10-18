def check_even_or_odd():
    number = int(input("შეიყვანეთ რიცხვი: "))
    
    if number % 2 == 0:
        print(f"{number} არის ლუწი.")
    if number % 2 != 0:
        print(f"{number} არის კენტი.")
        
# ფუნქციის გამოძახება
check_even_or_odd()
