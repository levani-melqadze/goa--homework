def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "არასწორი ოპერაცია"


def max_number(numbers):
    return max(numbers)


def min_number(numbers):
    return min(numbers)


def letter_position(name):
    if name:
        first_letter = name[0].lower()
        return ord(first_letter) - ord('a') + 1
    return None


def greet():
    return "გამარჯობა! 😉"
