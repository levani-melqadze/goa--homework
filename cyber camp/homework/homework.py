
films1 = input("Enter your 3 favorite films: ")
films2 = input("Enter your 3 favorite films: ")
films3 = input("Enter your 3 favorite films: ")

color1 = input("Enter your favorite 3 colors: ")
color2 = input("Enter your favorite 3 colors: ")
color3 = input("Enter your favorite 3 colors: ")

number1 = input("Enter your favorite 3 numbers: ")
number2 = input("Enter your favorite 3 numbers: ")
number3 = input("Enter your favorite 3 numbers: ")

country1 = input("Enter your favorite 3 countries: ")
country2 = input("Enter your favorite 3 countries: ")
country3 = input("Enter your favorite 3 countries: ")

# Menu for user choice
print("Choose what you want to print:")
print("a. Films")
print("b. Numbers")
print("c. Countries")
print("d. Colors")
choice = input("Enter your choice (a/b/c/d): ")

if choice == "a":
    print(films1, films2, films3)
elif choice == "b":
    print(number1, number2, number3)
elif choice == "c":
    print(country1, country2, country3)
elif choice == "d":
    print(color1, color2, color3)
else:
    print("Invalid choice. Please choose a, b, c, or d.")


while True:
    print("Choose what you want to display:")
    print("a. Films")
    print("b. Numbers")
    print("c. Countries")
    print("d. Colors")
    print("e. Exit")
    choice = input("Enter your choice (a/b/c/d/e): ")

    if choice == 'a':
        film1 = input("Enter your favorite film 1: ")
        film2 = input("Enter your favorite film 2: ")
        film3 = input("Enter your favorite film 3: ")
        print(f"Your favorite films are: {film1}, {film2}, and {film3}")
    elif choice == 'b':
        number1 = input("Enter your favorite number 1: ")
        number2 = input("Enter your favorite number 2: ")
        number3 = input("Enter your favorite number 3: ")
        print(f"Your favorite numbers are: {number1}, {number2}, and {number3}")
    elif choice == 'c':
        country1 = input("Enter your favorite country 1: ")
        country2 = input("Enter your favorite country 2: ")
        country3 = input("Enter your favorite country 3: ")
        print(f"Your favorite countries are: {country1}, {country2}, and {country3}")
    elif choice == 'd':
        color1 = input("Enter your favorite color 1: ")
        color2 = input("Enter your favorite color 2: ")
        color3 = input("Enter your favorite color 3: ")
        print(f"Your favorite colors are: {color1}, {color2}, and {color3}")
    elif choice == 'e':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option (a/b/c/d/e).")

# Prompting the user to exit the program
exit_choice = input("Do you want to exit? (yes/no): ")
if exit_choice.lower() == 'yes':
    print("Exiting program...")
