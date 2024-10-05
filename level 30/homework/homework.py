names = ["გაბრიელ", "ალექსანდრე", "მიხეილ", "ნინო", "თამარი", "სოფიო", "ილია", "კატერინე", "ლუკა", "მარიამი"]
filtered_names = []

for name in names:
    if len(name) <= 10:
        filtered_names.append(name)

print(filtered_names)


#
user_number = int(input("შეიყვანეთ რიცხვი: "))
numbers_list = []

for i in range(1, user_number + 1):
    numbers_list.append(i)

print(numbers_list)

#
foods = ["პური", "ყველი", "ვაშლი", "ბანანი", "ყურძენი"]
cars = ["Toyota", "BMW", "Mercedes", "Audi", "Honda"]

combined_list = foods + cars
print(combined_list)

#

fruits = ["ვაშლი", "ბანანი", "ქლიავი", "კალამანი", "ძეხვი", "ყურძენი", "პური", "კიტრი"]
non_fruits = ["ძეხვი", "პური", "კიტრი"]

for item in non_fruits:
    fruits.remove(item)

print(fruits)


#


initial_list = [3, 8, 15, 22, 37, 44, 57, 62, 73, 84, 91, 100, 2, 31, 16, 75, 42, 51, 66, 29]


even_numbers = []
odd_numbers = []


for num in initial_list:
    if num % 2 == 0:
        even_numbers.append(num) 
    else:
        odd_numbers.append(num)  


print("ლუწი რიცხვები:", even_numbers)
print("კენტი რიცხვები:", odd_numbers)
