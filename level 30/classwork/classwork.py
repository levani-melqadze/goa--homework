
mentors = ["გიორგი", "ნინო", "ლევან", "თამარი"]


regular_names = []

name = input("შეიყვანეთ სახელი: ")


if name in mentors:
    mentors.append(name)  
else:
    regular_names.append(name)  


print("მენტორები:", mentors)
print("ჩვეულებრივი სახელები:", regular_names)
