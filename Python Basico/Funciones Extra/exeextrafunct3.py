phrase=input("Please enter a phrase: ")

def vowel_counter(phrase):
    vowels="aeiou"
    counter=0
    for word in phrase.lower():
            if word in vowels:
                counter+=1
    return counter

result=vowel_counter(phrase)
print(f"The number of vowels in your phrase, is {result}")
