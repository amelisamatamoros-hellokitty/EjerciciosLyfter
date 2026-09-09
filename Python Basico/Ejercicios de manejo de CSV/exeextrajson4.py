import json

def json_reader():
    file_path=input('Enter the file path for your json file:  ')
    with open(file_path,'r') as file:
        data=json.load(file)
    return data

def pokemon_types(pokemon_list):
    type_counter={}
    for pokemon in pokemon_list:
        pokemon_type=pokemon['type']
        type_counter[pokemon_type]=type_counter.get(pokemon_type,0)+1
        level_counter+=pokemon['level']

    return type_counter


def result(new_list):
    for type,average in new_list.items():
        print(f'Type: {type} -- Level average: {average}')

def main():
    my_pokemon_list=json_reader()
    my_first_result=pokemon_types(my_pokemon_list)
    result(my_first_result)


if __name__=='__main__':
    main()



