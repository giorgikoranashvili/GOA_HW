password = "1234"  # განსაზღვრული პაროლი

for attempt in range(3):
    user_input = input("Please enter the password: ")
    if user_input == password:
        print("correct")
        break
else:
    print("out of trys")