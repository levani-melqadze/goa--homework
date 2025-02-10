def calculate():
  
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    
   
    print(f"ჯამი: {num1 + num2}")
    print(f"სხვაობა: {num1 - num2}")
    print(f"გამრავლება: {num1 * num2}")
    
    if num2 != 0:
        print(f"გაყოფა: {num1 / num2}")
        print(f"ნაშთი: {num1 % num2}")
    else:
        print("გაყოფა 0-ზე შეუძლებელია")


calculate()

