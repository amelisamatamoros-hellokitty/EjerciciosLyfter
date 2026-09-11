print("---This program will help you create a list of 5 words and will filter the ones with more then 4 characters---")
word_list=[]
for number in range(5):
    single_word=input(f"Please enter word number {number+1}: ")
    word_list.append(single_word)
print(f"Your list of words is: {word_list}")
new_list=[]
for index in range(len(word_list)):
    inner_string=word_list[index]
    if len(inner_string)>4:
        new_list.append(inner_string)
    else:
        continue
print(f"The words with more than 4 characters, are: {new_list})")