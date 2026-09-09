print("---With this program we will review a list and determine which is the minimun number in the list---")
my_list=[]
list_lenght=int(input("Please provide the ammount of numbers you want to add to your list "))
for number in range(list_lenght):
    number=int(input(f"Please provide number {number+1}: "))
    my_list.append(number)
print(f"the list of numbers you provided is: {my_list}")
minimum=my_list[0]
for index in range(0,len(my_list)):
    if my_list[index]<min:
        minimum=my_list[index]
    else:
        continue
print(f"The lowest value in your list, is: {minimum}")