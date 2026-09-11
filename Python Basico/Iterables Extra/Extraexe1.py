print("---With this program I will let you know how many times a number can be found in a list---")
my_list=[]
list_range=int(input("Please enter how many numbers you want in your list: "))
for number in range(list_range):
    number=int(input(f"Please provide number{number+1}: "))
    my_list.append(number)
number_to_find= int(input("Please provide the number you want to search in the list that's above: "))
rep=0
for number in my_list:
    if number==number_to_find:
        rep+=1
    else:
        rep=rep
print(f"This is the list you provided:{my_list}")
print(f"The number {number_to_find} is found {rep} times in the provided list")