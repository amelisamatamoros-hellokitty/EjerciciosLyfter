print("----Guess the secret number----")
import random
secret_number = random.randint(1, 10)
number=int(input("please enter a number between 1 and 10"))
while secret_number!=number:
    number=int(input("You have not guessed the secret number, please enter another number"))
print(f"You have guessed the secret number: {number}")



