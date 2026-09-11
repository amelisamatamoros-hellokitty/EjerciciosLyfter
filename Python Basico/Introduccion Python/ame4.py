print("----determine the highest number----")
num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))
num3=int(input("Please enter the third number: "))
if num1>=num2 and num1>=num3:
    print(f"the highest number is {num1}")
elif num2>=num1 and num2>=num3:
    print(f"the highest number is {num2}")
elif num3>=num1 and num3>=num2:
    print(f"the highest number is {num3}")
    