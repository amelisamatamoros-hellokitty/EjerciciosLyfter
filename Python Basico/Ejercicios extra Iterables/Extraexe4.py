print("---With this program we will determine the average of a list and then we will create a new list with---")
my_list=[]
while True:
    number=input("Enter a number o press Enter to finish: ")
    if number=="":
        break
    my_list.append(int(number))
print(f"Your list is {my_list}")
total=0
counter=1
while counter<=len(my_list):
    total+=my_list[counter-1]
    counter+=1
average=total/len(my_list)
new_list=[]
for number in my_list:
    if number>average:
        new_list.append(number)
    else:
        continue
print(f"The average of your list is: {average}")
print("The new list is", new_list)
