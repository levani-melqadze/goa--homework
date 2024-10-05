

mentors = ['გაბრიელ', 'ანა', 'ლევანი', 'მარიამი', 'თემო']


regular_names = []


for _ in range(3): 
    name = input("შეიყვანეთ სახელი: ")
    
  
    if name in mentors:
        print(name + " არის მენტორი.")
    else:
   
        regular_names.append(name)
        print(name + " დაემატა ჩვეულებრივი სახელების სიაში.")

print("მენტორების სია:", mentors)
print("ჩვეულებრივი სახელების სია:", regular_names)

