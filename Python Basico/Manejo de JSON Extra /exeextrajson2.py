import json

def json_reader():
    data=[]        
    try:    
        file_path=input('Enter the file path of your json file:  ')
        with open(file_path,'r') as file:
            data=json.load(file)
        return data
    except json.JSONDecodeError:
        print('Invalid JSON file')
    except FileNotFoundError:
        print('file not found') 

def ask_pokemon(my_data):
    pokemon_types=['Normal','Fire','Water','Grass','Electric','Ice','Fighting','Posion','Ground','Flying','Psychic','Bug','Rock','Ghost','Dragon','Dark','Steel','Fairy','Stellar']
    new_pokemon_type_list = [text.lower() for text in pokemon_types]
    pokemon_name=''
    while True:
        ask=input('Enter the type of pokemon you want to search:  ')
        if ask.lower() in new_pokemon_type_list:
            break
        else:
            print('Pokemon type is not valid')
    print('The pokemons found under this type, are:')
    for pokemon in my_data:
        if pokemon['type'].lower()==ask.lower():
            pokemon_name+="\n"+pokemon['name']+"\n" 
    if pokemon_name=='':
        print('There were no pokemons found for this type')
    return pokemon_name

def main():
    my_file=json_reader()
    while my_file is None:
        my_file=json_reader()
        if my_file is not None:
            break
    result=ask_pokemon(my_file)
    print(result)

if __name__=='__main__':
    main()

