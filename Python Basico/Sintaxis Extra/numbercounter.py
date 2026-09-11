print("---number counter---")
number=int(input("Please enter a number: "))
counter=1
total_sum=0
while counter<=number:
    total_sum=total_sum+counter
    counter=counter+1
print(f"the sum of all the numbers contained in {number} is {total_sum}")
