my_list=[]
while True:
    number=input("Please enter a number to add to your list or press enter to finish: ")
    if number=="":
        break
    my_list.append(int(number))
print(f"The list you entered, is: {my_list}")

def sum_of_my_list(my_list):
    item=0
    inner_sum=0
    while item < len(my_list):
        inner_sum+=my_list[item]
        item+=1
    return inner_sum

result=sum_of_my_list(my_list)
print(f"The sum of the numbers in your list, is: {result}")       

