try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("შეცდომა: ნულზე გაყოფა შეუძლებელია!")

try:
    data = {"სახელი": "გაბრიელ"}
    print(data["ასაკი"])
except KeyError:
    print("შეცდომა: გასაღები არ არსებობს!")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("შეცდომა: ინდექსი არასწორია!")
