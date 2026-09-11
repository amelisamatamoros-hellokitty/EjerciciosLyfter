my_list=[]
while True:
    number=input("Input the elements you want in the list, press enter when finished: ")
    if number=="":
        break
    my_list.append(number)
print(f"This is your list= {my_list}")

def float_converter(my_list):
    float_sum=0
    for item in my_list:
        try:
            float_item=float(item)    
            float_sum+=float_item
            print(f"{float_item} was correctly added")
        except ValueError as error:
            print(f"Invalid element {item}")
    print(f"The total summatory is {float_sum}")
    return float_sum

float_converter(my_list)