import json

def json_reader():
    data=[]
    try:
        file_path=input('Enter the path of the JSON file:  ')
        with open(file_path,'r') as file:
            data=json.load(file)
            return data
    except json.JSONDecodeError:
        print('Invalid JSON file')
    except FileNotFoundError:
        print('file not found')


def pokemon_info():
    skills=[]
    stats={}
    pokemon={}
    pokemon['name']=input('Enter the name of the pokemon:  ')
    print('''Types of Pokemon:
    1. Normal
    2.Fire
    3.Water
    4.Grass
    5.Electric
    6.Ice
    7.Fighting
    8.Posion
    9. Ground
    10. Flying:
    11. Psychic
    12. Bug
    13. Rock
    14. Ghost
    15. Dragon
    16. Dark
    17. Steel
    18. Fairy
    19. Stellar''')
    pokemon['type']=input('Enter the type of pokemon:  ')
    pokemon['level']=int(input('Enter the level of the pokemon (0 - 100):  '))
    pokemon['weight_kg']=float(input('Enter the weight in kgs:  '))
    pokemon['is_shiny']=input('Is the pokemon shiny? (True/False):   ')
    pokemon['held_item']=input('Enter the held item of the pokemon:  ')
    for item in range(4):
        skill=input(f'Enter skill no.{item+1}:   ')
        skills.append(skill)
    pokemon['skills']=skills
    stats['hp']=input('Enter the hp of the pokemon(1 HP -714 HP):  ')
    stats['attack']=input('Enter the attack of the pokemon(4-504):  ')
    stats['defense']=input('Enter the defense of the pokemon(4-614):  ')
    stats['sp_attack']=input('Enter the special attack of the pokemon(4-535):  ')
    stats['sp_defense']=input('Enter the special defense of the pokemon(4-614):  ')
    stats['speed']=input('Enter the speed of the pokemon(4-548):  ')
    pokemon['stats']=stats
    return pokemon

def add_pokemon(data,pokemon):
    data.append(pokemon)
    return data

def save_pokemon_list(data):
    file_path=input('Enter the path to save the JSON file:  ')
    with open(file_path,'w',encoding="utf-8") as file:
        new_json=json.dump(data,file)
        return new_json


def main():
    my_data=json_reader()
    while my_data is None:
        my_data=json_reader()
        if my_data is not None:
            break
    pokemon=pokemon_info()
    result=add_pokemon(my_data,pokemon)
    print('Pokemon was added succesfully to the python file')
    print(result)
    my_json=save_pokemon_list(result)
    print('File successfully converted to a json object')


if __name__=='__main__':
    main()