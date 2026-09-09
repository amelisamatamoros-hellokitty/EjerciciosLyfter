import csv

def list_creator():
    my_videogames=[]
    while True:
        unique_videogame={}
        try: 
            decision=input('Would you like to submit a videogame? (Y/N) ')
            if decision=='y' or decision=='Y':
                unique_videogame['name']=input('Please input the name of the videogame:  ')
                unique_videogame['genre']=input('Please input the genre of the videogame:  ')
                unique_videogame['developer']=input('Please input the developer of the videogame:  ')
                unique_videogame['classification']=input('Please input the classification of the videogame:  ')
                my_videogames.append(unique_videogame)   
            elif decision=='n'or decision=='N':
                break
            else:
                raise ValueError('Submitted option is not valid') 
        except ValueError as error:
            print(error) 
    return my_videogames


def csv_creator(file_path,data):
    with open(file_path,'w', encoding='utf-8',newline='') as file:
        headers=data[0].keys()
        writer=csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)           

        

def main():
    while True:
        my_list=list_creator()
        if my_list:
            csv_creator('my_videogames.csv',my_list)
            break  
        else:
            print("To start the program, you should submit a videogame's information")

        
if __name__ == '__main__':
    main()

