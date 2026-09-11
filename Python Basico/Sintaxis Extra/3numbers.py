print("Please enter 3 numbers")
num1=int(input("Number 1:"))
num2=int(input("Number 2:"))
num3=int(input("Number 3:"))
if num1==30 or num2==30 or num3==30:
    print("Correct")
elif num1+num2+num3==30:
    print("Correct")
else:
    print("Incorrect")
