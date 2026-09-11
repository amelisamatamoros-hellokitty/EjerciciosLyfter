my_string=input("Please write a line of letters and press enter when finished ")
print(f"the line you entered is:{my_string}")


def find_upper(my_string):
    new_string=my_string.replace(" ","")
    number_upper=0
    for char in new_string:
        if char.isupper()==True:
            number_upper+=1
    number_lower=len(new_string)-number_upper
    return number_upper,number_lower


result_upper, result_lower=find_upper(my_string)
print(result_upper)
print(f"(There's {result_upper} upper cases and {result_lower} lower cases)")

