print("Welocme to my math quiz!")

playing = input("Do you want to play a game?  ")

if playing != "yes":
    quit()

print("Okay! Lets play :)")

import random

number1 = random.randint(0,12)
number2 = random.randint(0,12)

result = number1 * number2
guess = input(f"what is {number1} x {number2} ?  ")
guess = int(guess)

if guess == result:
    print ("Great job! You got the right answer!")
else:
    print ("Not quite. Try again.  Practice makes perfect!")

