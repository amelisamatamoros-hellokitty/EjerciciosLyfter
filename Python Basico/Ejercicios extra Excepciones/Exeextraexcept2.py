my_list=[]
while True:
    number=input("Please enter a number for your list, when finished, press Enter: ")
    if number=="":
        break
    my_list.append(number)
print(f"Your submitted list is {my_list}")

def int_converter(my_list):
    for char in my_list:
        try:
            int_char=int(char)
            print(f"{char} is converted to {int_char}")
        except ValueError:
            print(f"The element {char} couldn't be converted to integer")
    return int_char

int_converter(my_list)


