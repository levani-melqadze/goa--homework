user_data = {}

# First name input
first_name = ""
while not first_name.isalpha():  # Check if only alphabets are entered
    first_name = input("Enter your first name: ")
    if not first_name.isalpha():
        print("Invalid input. Please enter a valid first name (alphabets only).")
user_data['First Name'] = first_name

# Last name input
last_name = ""
while not last_name.isalpha():  # Check if only alphabets are entered
    last_name = input("Enter your last name: ")
    if not last_name.isalpha():
        print("Invalid input. Please enter a valid last name (alphabets only).")
user_data['Last Name'] = last_name

# Phone number input
phone = ""
while not (phone.isdigit() and len(phone) == 10):  # Check if it's a 10-digit number
    phone = input("Enter your phone number (10 digits): ")
    if not (phone.isdigit() and len(phone) == 10):
        print("Invalid phone number. Please enter a valid 10-digit phone number.")
user_data['Phone Number'] = phone

# Email input
email = ""
while not ('@' in email and '.' in email):  # Simple email validation
    email = input("Enter your email: ")
    if not ('@' in email and '.' in email):
        print("Invalid email. Please enter a valid email address.")
user_data['Email'] = email

# Age input
age = ""
while not (age.isdigit() and 18 <= int(age) <= 100):  # Check if age is between 18 and 100
    age = input("Enter your age (between 18 and 100): ")
    if not (age.isdigit() and 18 <= int(age) <= 100):
        print("Invalid age. Please enter a number between 18 and 100.")
user_data['Age'] = age

# Gender input
gender = ""
while gender.lower() not in ['male', 'female', 'other']:  # Check if a valid gender is selected
    gender = input("Select your gender (Male/Female/Other): ")
    if gender.lower() not in ['male', 'female', 'other']:
        print("Invalid selection. Please choose from Male, Female, or Other.")
user_data['Gender'] = gender.capitalize()

# Display user data
print("\nRegistration Complete!")
print("Here is your information:")
for key, value in user_data.items():
    print(f"{key}: {value}")