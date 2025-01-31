#Mutable მონაცემთა ტიპები: List, Dictionary, Set.

#mmutable მონაცემთა ტიპები: Tuple, String, Integer, Float, Boolean.

#Lambda ფუნქციის მეორე სახელი: ანონიმური ფუნქცია.

#განსხვავება map და filter შორის:

#Map: გამოყენებულია მისამართით ფუნქციის ნებისმიერი მნიშვნელობის განსახორციელებლად თითოეული ელემენტისათვის, ამ შედეგებს ახალი სიაში აგზავნის.
#Filter: გამოიყენება მხოლოდ ისეთი ელემენტების არჩევისთვის, რომლებიც აკმაყოფილებენ მოცემულ პირობას.
#ორი სტრინგის შეერთება: Concatenation.'



numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)


celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda x: x * 33.8 + 32, celsius))
print(fahrenheit)


