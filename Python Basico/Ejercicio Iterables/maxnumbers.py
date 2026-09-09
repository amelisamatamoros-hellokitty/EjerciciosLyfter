numbers=[]
print("Please enter 10 numbers")
for counter in range(10):
    number=int(input(f"Number {counter+1}: "))
    numbers.append(number)
max_number=numbers[0]
for num in numbers:
    if num>max_number:
        max_number=num
print(f"The numbers you submitted, are:{numbers}")
print(f"The highest number you submitted, is: {max_number}")