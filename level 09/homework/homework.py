# მომხმარებლის მონაცემების მიღება
current_age = int(input("გთხოვთ, შეიყვანოთ თქვენი ამჟამინდელი ასაკი: "))
current_year = int(input("გთხოვთ, შეიყვანოთ მიმდინარე წელი: "))
travel_years = int(input("რამდენი წლით გსურთ დროში მოგზაურობა? "))

# დროში მოგზაურობის შედეგის გამოთვლა
future_year = current_year + travel_years
future_age = current_age + travel_years

# შედეგის დაბეჭდვა
print(f"დროში მოგზაურობის შემდეგ წელი იქნება: {future_year}")
print(f"თქვენი ასაკი იქნება: {future_age} წელი")
