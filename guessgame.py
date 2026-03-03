import random
num=random.randint(1,30)


guess=int(input("Can you guess the number:"))
while(num!=guess):
    
    if(guess>num):
        print("your guess is higher than number")
    else:
        print("your guess is lower than number")
    guess=int(input("Guess again:"))

print("You won")