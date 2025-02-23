# 1
# List (ლისტი) არის მონაცემთა სტრუქტურა, რომელიც შენახავს ელემენტებს ერთ სისტემაში. მასში შეიძლება იყოს სხვადასხვა ტიპის მონაცემები (მხოლოდ Python-ში). მაგალითად: რიცხვები, სტრიქონები, ლოგიკური მნიშვნელობები და სხვა.

# Indexing (ინდექსირება) ნიშნავს ლისტის ელემენტების მისაღებად ინდექსის გამოყენებას. ინდექსი არის ნომერი, რომელიც მიუთითებს ელემენტის პოზიციას. Python-ში ინდექსი იწყება 0-დან, ანუ პირველი ელემენტი აქვს ინდექსი 0, მეორე - 1 და ასე შემდეგ.

# Slicing (სლაისინგი) არის მეთოდი, რომელიც საშუალებას გვაძლევს მივიღოთ ლისტის ელემენტების გარკვეული ნაწილი, დაწყებული ერთი ინდექსიდან და დასრულებული მეორე ინდექსამდე.

# 2
my_list = [3.14, "hello", 42, True, [1, 2, 3]]

# დადებითი ინდექსები
print(my_list[0])  # 3.14
print(my_list[1])  # hello
print(my_list[2])  # 42
print(my_list[3])  # True
print(my_list[4])  # [1, 2, 3]

# ნეგატიური ინდექსები
print(my_list[-1])  # [1, 2, 3]
print(my_list[-2])  # True
print(my_list[-3])  # 42
print(my_list[-4])  # hello
print(my_list[-5])  # 3.14

# 3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# აიღე პირველი 5 ელემენტი
print(my_list[:5])  # [1, 2, 3, 4, 5]

# აიღე ელემენტები ინდექსებიდან 3-დან 8-მდე (8 არ შედის)
print(my_list[3:8])  # [4, 5, 6, 7, 8]

# 4
my_list = [10, 20, 30, 40, 50, 60]

# აიღე ყველა ელემენტი ყოველი მეორე ინდექსისგან
print(my_list[::2])  # [10, 30, 50]