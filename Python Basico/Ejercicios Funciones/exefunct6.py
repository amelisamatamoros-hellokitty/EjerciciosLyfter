my_string=input("Please input a groupd of words, separated by a dash: ")
word_list=my_string.split('-')

def order_list(word_list):
    word_list.sort()
    result="-".join(word_list)
    return result

result_2=order_list(word_list) 
print(result_2)



