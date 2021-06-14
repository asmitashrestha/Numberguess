import random

number=input("Enter a number of your choice :")

if number.isdigit():
    number=int(number)

    if number>=0:
        print("Please type a number smaller than the entered number :")
    else:
        print("Please enter a number next time :")

    random_number=random.randint(0,number)
    guess=0

    while True:
        guess+=1
        guess_number=input("Enter a number that you guess :")
        if guess_number.isdigit():
            guess_number=int(guess_number)
        else:
            print("Please enter a number next time :")
            continue

        if guess_number==random_number:
            print("You have done it !!!")
            break
        elif guess_number>random_number:
            print("Your guess was too high !")
        else:
            print("Your guess is too low !!!")

        print("You got it",guess,"guess")        

