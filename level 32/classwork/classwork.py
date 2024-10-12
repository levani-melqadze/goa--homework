
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


middle_elements = my_list[6:9]  
print("შუაში მყოფი სამი ელემენტი:", middle_elements)


print("ელემენტები 2-დან 7-მდე:", my_list[2:8])


print("ელემენტები თავიდან 7-მდე:", my_list[:8])


print("ელემენტები 7 ინდექსიდან ბოლომდე:", my_list[7:])




#





names = ["ანა", "ბენჯი", "გაბრიელი", "სესილი", "დავით", "ელენე", "ზურაბი", "ილია", "კატია", "მართა"]


filtered_names = []


for name in names:
    if not name.startswith("ა"):
        filtered_names.append(name)


print("გაფილტრული სია:", filtered_names)
