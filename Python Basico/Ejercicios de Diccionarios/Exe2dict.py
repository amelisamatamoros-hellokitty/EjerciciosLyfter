list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
user_data={}
for item in range (len(list_a)):
    user_data[list_a[item]]=list_b[item]
print(user_data)