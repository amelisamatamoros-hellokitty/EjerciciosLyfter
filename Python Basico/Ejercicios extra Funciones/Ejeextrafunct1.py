word=(input("Please enter a word:  "))
char=(input("Please enter the character you want to find in the word you submitted. "))   
print(word)
print(char)


def find_char(word,char):
    count_char=0
    for item in word.lower():
        if item==char.lower():
            count_char+=1    
    return count_char


total=find_char(word,char)
print(f"The character was found {total} times in the word")
