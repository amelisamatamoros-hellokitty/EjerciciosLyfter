def name_reviewer():
    while True: 
        try:
            name=input("Please enter your name:   ")
            if any(character.isdigit() for character in name)==False:
                print(f"Welcome {name}")
                return name
            else:
                raise ValueError
        except ValueError as error:
            print("Your name can't be a number")

def age_reviewer():
    while True:
        try:
            age=int(input("Please enter your age: "))
            if 0<age<100:
                print('Thank you for submitting your age')
                return age
            else:
                print("The submitted number is incorrect,please try again")
        except ValueError as error:
            print("Invalid number")


print(f"Hi {name_reviewer()}, your age is {age_reviewer()}")