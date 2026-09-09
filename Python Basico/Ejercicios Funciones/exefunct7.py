number_list=[]
while True:
    number=input("Please enter the numbers of your list and when finished, press enter: ")
    if number=="":
        break
    number_list.append(int(number))
print(f"Your list of numbers is {number_list}")

def is_prime(number):
    if number<2:
        return False
    for item in range(2,(number-1)):
        if number%item==0:
            return False
    return True

prime_list=[]
for n in number_list:
    result=is_prime(n)
    if result==True:
        prime_list.append(n)
    else:
        continue

print(f"The prime numbers in your list, are: {prime_list}")

             
