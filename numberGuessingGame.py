import random

print("Number Guessing Game")
number=random.randint(1,9)
guess=int(input("Guess a number between 1 to 9:"))
if(guess < number):
    print("guess a number higher than",guess)
   
elif(guess > number):
    print("guess a number lower than",guess)

else:
    print("CONGRATULATIONS! your guess",guess,"is correct")