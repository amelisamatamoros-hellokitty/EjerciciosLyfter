import json

def json_reader():
    data=[]
    try:
        file_path=input('Enter the file path for your json file:  ')
        with open(file_path,'r') as file:
            data=json.load(file)
            return data
    except json.JSONDecodeError:
        print('Invalid JSON file')
    except FileNotFoundError:
        print('file not found')

def pokemon_types(pokemon_list):
    type_counter={}
    level_counter={}
    new_list={}
    for pokemon in pokemon_list:
        pokemon_type=pokemon['type']
        type_counter[pokemon_type]=type_counter.get(pokemon_type,0)+1
        level_counter[pokemon_type]=level_counter.get(pokemon_type,0)+pokemon['level']
    for type in type_counter:
        new_list[type]=level_counter[type]/type_counter[type]
    return new_list


def result(new_list):
    for type,average in new_list.items():
        print(f'Type: {type} -- Level average: {average}')

def main():
    my_pokemon_list=json_reader()
    while my_pokemon_list is None:
        my_pokemon_list=json_reader()
        if my_pokemon_list is not None:
            break
    my_first_result=pokemon_types(my_pokemon_list)
    result(my_first_result)


if __name__=='__main__':
    main()



