def menu():
    print("""
    ---Main Menu---
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Erase result
    6. Exit
    """)


def number_reviewer():
    while True:
        try:
            num_one=int(input("Enter your first number: "))
            return num_one
        except ValueError:
            print("The submitted number is not applicable")


def my_calculator(num_one):
    selection=0
    while True:
        try:
            selection=int(input("Please select an option of the menu (1-6): "))
            if selection<1 or selection>6:
                raise AttributeError
            else:
                break
        except ValueError:
            print("The selected option is not valid")
        except AttributeError:
            print("The selected option is not available")    
    if selection==5:
        print("result is erased")
        num_one="Erase"
        return num_one
    if selection==6:
        print("You have chosen to exit, good bye!")
        num_one="Exit"
        return num_one

    while True:
        try:
            num_two=int(input("Enter your second number: "))
            operation=0
            if selection==1:
                operation=num_one+num_two
            elif selection==2:
                operation=num_one-num_two
            elif selection==3:
                operation=num_one*num_two
            elif selection==4 and num_two!=0:
                operation=num_one/num_two
            elif selection==4 and num_two==0:
                operation="Zero"
                raise ZeroDivisionError
        except ValueError:
            print("The selected option is not valid")
        except ZeroDivisionError:
            print("The number can't be divided by zero")
        if operation!="Zero":
            print(f"The result of your operation, is: {operation}")
        return operation        


def main():
    menu()
    my_number=number_reviewer()

    while True:
        result=my_calculator(my_number)
        if result=="Erase":
            my_number=number_reviewer()
        elif result=="Exit":
            break
        elif result=="Zero":
            number_reviewer()
        else:
            my_number=result

if __name__ == '__main__':
    main()