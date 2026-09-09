print("---Determine your life stage---")

import re
while True:
    name=input("Please enter your first and last name: ")
    if re.fullmatch(r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", name) and len(name) >= 2:
        print(f"Hi, {name.strip()}!")
        break
    else:
        print("Error: Invalid name.")
age=int(input("Please enter your age: "))
if age <=2:
    print(name + ", you are a baby")
elif(age<=10):
    print(name + ", you are a child")
elif(age<=12):
    print(name + ", you are a preteen")
elif(age<=19):
    print(name, "you are a teenager")
elif age<=40:
    print(name+", you are a young adult")
elif age<=64:
    print(name+", you are an adult")
else:
    print(name+", you are an older adult")



