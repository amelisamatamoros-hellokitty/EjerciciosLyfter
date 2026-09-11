my_string=input("Please enter the phrase you want to turn around: ")

def reverse_string(my_string):
    new_string=""
    for letter in range((len(my_string))-1,-1,-1):
        new_string+= (my_string[letter])
    return new_string

result=reverse_string(my_string)
print(result)



