import random
import sys

random_number = random.randint(1, 10)

while True:
    
    user_choice = input("Guess the number: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
    else:
        sys.exit("Enter a valid number")
    try:
        if int(user_choice) < random_number:
            print("Guess the number that is higher then this one")
        elif int(user_choice) > random_number:
            print("Guess the number that is lower then this one")
        else:
            print("You guessed the number correctly!") 
            break
            
        print("Try again!")
    except KeyboardInterrupt:
        sys.exit(0)
