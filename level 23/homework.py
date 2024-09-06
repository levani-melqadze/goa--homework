user_data = {}

# First name input
while True:
    first_name = input("Enter your first name: ")
    if first_name.isalpha():  # Check if only alphabets are entered
        user_data['First Name'] = first_name
        break
    else:
        print("Invalid input. Please enter a valid first name (alphabets only).")

# Last name input
while True:
    last_name = input("Enter your last name: ")
    if last_name.isalpha():  # Check if only alphabets are entered
        user_data['Last Name'] = last_name
        break
    else:
        print("Invalid input. Please enter a valid last name (alphabets only).")

# Phone number input
while True:
    phone = input("Enter your phone number (10 digits): ")
    if phone.isdigit() and len(phone) == 10:  # Check if it's a 10-digit number
        user_data['Phone Number'] = phone
        break
    else:
        print("Invalid phone number. Please enter a valid 10-digit phone number.")

# Email input
while True:
    email = input("Enter your email: ")
    if '@' in email and '.' in email:  # Simple email validation
        user_data['Email'] = email
        break
    else:
        print("Invalid email. Please enter a valid email address.")

# Age input
while True:
    age = input("Enter your age (between 18 and 100): ")
    if age.isdigit() and 18 <= int(age) <= 100:  # Check if age is between 18 and 100
        user_data['Age'] = age
        break
    else:
        print("Invalid age. Please enter a number between 18 and 100.")

# Gender input
while True:
    gender = input("Select your gender (Male/Female/Other): ").lower()
    if gender in ['male', 'female', 'other']:  # Check if a valid gender is selected
        user_data['Gender'] = gender.capitalize()
        break
    else:
        print("Invalid selection. Please choose from Male, Female, or Other.")

# Display user data
print("\nRegistration Complete!")
print("Here is your information:")
for key, value in user_data.items():
    print(f"{key}: {value}")
