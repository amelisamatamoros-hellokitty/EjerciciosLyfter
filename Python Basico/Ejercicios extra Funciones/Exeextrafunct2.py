word_list=input("Please enter a list of words, separated by a space:  ")
char_number=int(input("What's the minimum letters you want to see in your word list?:  "))
final_list=word_list.split()

def arrange_list(final_list,char_number):
    new_list=[]
    for item in final_list:
        if len(item)>char_number:
            new_list.append(item)
        else:
            continue
    return new_list

result=arrange_list(final_list,char_number)
print(f"The words with a minimum of {char_number} characters, is: {result}")

