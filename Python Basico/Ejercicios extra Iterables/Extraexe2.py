print("---with this program, we will verify if all your submitted numbers are positive---")
my_list=[]
all_true=True
list_length=int(input("How many numbers would you like to add to your list?: "))
for index in range(list_length):
    number=int(input(f"Number {index+1}: "))
    my_list.append(number)
for number in my_list:
    if number<=0:
        print("there is at least one number that's negative or cero")
        all_true=False
        break
    else:
        continue
if all_true==True:
    print("All numbers are positive") 
    


