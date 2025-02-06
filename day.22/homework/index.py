# 1
password = "1234"  # განსაზღვრული პაროლი

for attempt in range(3):
    user_input = input("Please enter the password: ")
    if user_input == password:
        print("correct")
        break
else:
    print("out of trys")

# 2
import random

# შემთხვევითი რიცხვის შექმნა
target_number = random.randint(1, 100)

while True:
    user_guess = int(input("Guess the number: "))
    
    if user_guess == target_number:
        print("Correct! You guessed the right number.")
        break
    elif user_guess < target_number:
        print("The number is bigger.")
    else:
        print("The number is smaller.")

# 3
a = 5  # პირველი რიცხვი
b = 10  # მეორე რიცხვი

if a > b:
    for num in range(b + 1, a):
        print(num)
else:
    for num in range(a + 1, b):
        print(num)

