# Collect user inputs for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform all logical operations
results = {
    "num1 < num2 and num1 < num2": (num1 < num2) and (num1 < num2),
    "num1 < num2 and num1 > num2": (num1 < num2) and (num1 > num2),
    "num1 > num2 and num1 < num2": (num1 > num2) and (num1 < num2),
    "num1 > num2 and num1 > num2": (num1 > num2) and (num1 > num2),
    "num1 < num2 or num1 < num2": (num1 < num2) or (num1 < num2),
    "num1 < num2 or num1 > num2": (num1 < num2) or (num1 > num2),
    "num1 > num2 or num1 < num2": (num1 > num2) or (num1 < num2),
    "num1 > num2 or num1 > num2": (num1 > num2) or (num1 > num2),
}

# Print the results
for expression, result in results.items():
    print(f"{expression}: {result}")
