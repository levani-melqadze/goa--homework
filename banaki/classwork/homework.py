#first stage


a = 20
b = 25

if a > 15 and b > 15:
    print('both numbers are more than 15')
else:
    print('one or both numbers are less than 15')

#ორივე რიცხვი 15-ზე მეტია
#end stage






#second stage



a = input("Hello, What's your name? ")
b = input("What is your surname? ")

if (a == "levani" or a == "levani") and (b == "melqadze" or b == "melqadze"):
    print("I know you")
else:
    print("I don't know you")





#thired stage


a = int(input("Enter a number: "))

if a < -10:
    print("Number is less than -10")
elif a < -50:
    print("Number is between -10 and -50")
else:
    print("Number is greater than or equal to -50")



#fourth stage


username = input("შეიყვანეთ თქვენი სახელი: ")
password = input("შეიყვანეთ თქვენი პაროლი: ")

if username == "user" and password == "admin":
    print("თქვენ გაიარეთ ავტორიზაცია")
elif username == "user" or password == "admin":
    print("კიდევ სცადეთ")
else:
    print("ჰაკერი ხარ")



    #fifth stage

#0 1 2 3  4 5 6 7
a = [2,5,4,10,3,2,6,5]

print(a)
print(a[0])
print(a[2])
print([7])

print(len(a))
print(a[len(a) -1])

print(a[-2])
print(a)
a.append(100)

a.append(200)
print(a)


import random


a = random.randrange(5, 11)
print(a)








#six stage

import random

# Create an empty list
a = []

# Generate a random number between 0 and 99 inclusive
random_number = random.randrange(0, 100)

# Append the random number to the list
a.append(random_number)

print(a)


#create an empty list
#and apend ten random elements from 0-100
#use for loop

#while True:

    # Create an empty list
a = []

    # Generate a random number between 0 and 99 inclusive
random_number = random.randrange(0, 100)

    # Append the random number to the list
a.append(random_number)

print(a)



#create an emty list
#and the program must ask you 'enter the lenght of the list
#program must generate random number
#and add to the list
#use for loop

import random

# Ask the user to enter the length of the list
length = int(input("Enter the length of the list: "))

# Create an empty list
a = []

# Generate random numbers and add them to the list
for _ in range(length):
    random_number = random.randrange(0, 100)  # Generate a random number between 0 and 99 inclusive
    a.append(random_number)  # Append the random number to the list

# Print the final list
print("Generated list:", a)




#seven stage


#use the code above
#and rewrie odd number to one list
#and even numbers to another
# Convert the number to a string


# Sample list of numbers
numbers = [4, 6, 8, 5, 4, 2, 0, 1, 7]

# Initialize lists to store odd and even numbers
odd_numbers = []
even_numbers = []

# Iterate through each number in the list
for num in numbers:
    # Check if the number is odd or even
    if num % 2 != 0:
        odd_numbers.append(num)
    else:
        even_numbers.append(num)

# Print the results
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)





#eight stage




