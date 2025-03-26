# 1. ფუნქციის ახსნა კომენტარით:
# ფუნქცია არის კოდი, რომელიც ერთ კონკრეტულ დავალებას ასრულებს. 
# ფუნქციის შექმნისას მას ვაძლევთ სახელს და არგუმენტებს, რომლებიც ფუნქციის შიგნით გამოიყენება. 
# ფუნქცია შეიძლება გამოიძახოთ რამდენჯერაც გსურთ.

# 2. ფუნქცია სახელად add_numbers(x, b) - ჯამი
def add_numbers(x, b):
    return x + b

# 3. ფუნქცია სახელად Hello(name) - გამარჯობა
def Hello(name):
    print("გამარჯობა, " + name)

Hello("შენი სახელი")  # შეცვალე "შენი სახელი" შენი სახელი

# 4. ფუნქცია სახელად Multiply_Number(x, b) - გამრავლება
def Multiply_Number(x, b):
    return x * b

# 5. ფუნქცია სახელად calculate_four_numbers(a, b, c, d) - ოთხი ოპერაცია
def calculate_four_numbers(a, b, c, d):
    addition = a + b + c + d
    subtraction = a - b - c - d
    multiplication = a * b * c * d
    division = a / b / c / d if b != 0 and c != 0 and d != 0 else "Cannot divide by zero"
    
    return addition, subtraction, multiplication, division

# გამოყენება:
result = calculate_four_numbers(5, 2, 3, 4)
print(result)  # შედეგი: (14, -4, 120, 0.041666666666666664)
