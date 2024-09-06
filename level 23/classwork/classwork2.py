    
user_input = int(input("Please enter a number: "))


number = 1

while number <= user_input:
    if number % 2 == 0:
        print(str(number) + ' is even')
    else:
        print(str(number) + ' is odd')
    
   
    number += 1