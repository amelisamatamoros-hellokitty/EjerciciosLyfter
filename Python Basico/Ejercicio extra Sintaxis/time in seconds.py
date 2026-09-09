print("----determine your time in seconds to get to 10 min----")
number=int(input("Please enter a time in seconds"))
while number<0:
    number=int(input("please enter a correct time in seconds, must be above 0:"))
if number>600:
    print("Higher")
elif number==600:
    print("equal")
else:
    print(600-number)


