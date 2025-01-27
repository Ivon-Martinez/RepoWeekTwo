import getpass


original_pin = 1234
supplied_pin = input("Enter your PIN: ")
attempts = 3
count = 0

while count < attempts:
    supplied_pin = input("Enter your PIN: ")
    if original_pin == supplied_pin:
        print("Its the right pin")
    else:
        count += 1
        if attempts - count == 0:
            print("sorry you are logged out!")
            break
        print("Wrong PIN! You have" +" "+ str(attempts-count) + "attempts left.")



