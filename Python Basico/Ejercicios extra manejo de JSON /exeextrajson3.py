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


def pokemon_stats(pokemon_list):
    for pokemon in pokemon_list:
        print(f"Name: {pokemon['name']}")
        pokemon_stats=pokemon['stats']
        print(f"Health Points: {pokemon_stats['hp']}")
        print(f"Attack: {pokemon_stats['attack']}")
        print(f"Defense: {pokemon_stats['defense']}")
        print(f"Special Attack: {pokemon_stats['sp_attack']}")
        print(f"Special Defense: {pokemon_stats['sp_defense']}")
        print(f"Speed: {pokemon_stats['speed']}")

def main():
    result=json_reader()
    while result is None:
        result=json_reader()
        if result is not None:
            break
    pokemon_stats(result)
    

if __name__=='__main__':
    main()