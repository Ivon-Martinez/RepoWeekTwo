import getpass

supplied_pin = None
myPin = 1234
tries = 3
count = 0
# count2 = 3

# while count < tries:
#     supplied_pin = input("Enter your PIN: ")
#     if int(supplied_pin) == myPin:
#         print("Correct PIN")
#         break
#     else:
#         count+=1
#         # count2 -= 1
#         if tries - count == 0:
#             print("Wrong PIN! No more attempts")
#             break
#         print("Wrong PIN!" + " You have " + str(tries - count) + " more attempts")


while count < tries:
    supplied_pin = getpass.getpass(prompt="Enter your PIN: " , stream=None)
    if int(supplied_pin) == myPin:
        print("Correct PIN")
        break
    else:
        count+=1
        # count2 -= 1
        if tries - count == 0:
            print("Wrong PIN! No more attempts")
            break
        print("Wrong PIN!" + " You have " + str(tries - count) + " more attempts")