# პირველი

# რიცხვების სია
numbers = [10, 20, 30, 40, 50]

# სიის სიგრძე
length = len(numbers)

# სიგრძე გამრავლებული 2-ზე
result = length * 2

print("სიის სიგრძე გამრავლებული 2-ზე:", result)



# მეორე
names = ["ანა", "გიორგი", "მარიამი", "ნიკა", "ლანა", "თემო"]

# უბრალოდ დავბეჭდოთ მხოლოდ კენტ ინდექსზე მდგომები
print(names[1::2])


# მესამე
mixed_list = [10, "ანა", 3.14, "გიორგი", 5, "მარიამი", 2.71]

# სიაში სტრინგი ტიპის ელემენტების მოძებნა და მათივე დამატება
for item in mixed_list:
    if isinstance(item, str):
        mixed_list.append(item)

print(mixed_list)

# მეოთხე

names = ["ანა", "გიორგი", "მარიამი"]
upper_names = []

for name in names:
    upper_names.append(name.upper())

print(upper_names)

