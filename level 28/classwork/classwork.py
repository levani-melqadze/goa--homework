nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
nums_list = list(nums) 

print(nums_list[0])  
print(nums_list[2])  
print(nums_list[4])  
print(nums_list[6]) 
print(nums_list[8])  

#


vehicles = [
    "Toyota Corolla",
    "Honda Civic",
    "Ford Mustang",
    "Chevrolet Camaro",
    "BMW 3 Series",
    "Ducati Panigale",
    "Harley-Davidson Sportster",
    "Kawasaki Ninja",
    "Suzuki Hayabusa",
    "Mercedes-Benz C-Class",
    "Volkswagen Golf",
    "Audi A4",
    "Porsche 911",
    "Lamborghini Huracán",
    "Nissan Skyline",
    "Pizza",
    "Burger",
    "Sushi",
    "Pasta",
    "Salad"
]


for i in range(len(vehicles)):
    print(vehicles[i]) 


#

numbers = list(range(1, 21))


for i in range(len(numbers)):
    if numbers[i] % 2 == 0:  
        print(numbers[i])

