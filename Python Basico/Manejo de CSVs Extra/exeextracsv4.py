import csv

def ask_developer():
    developer=input("Please enter the name of a videogame developer: ")
    return developer


def file_reader(file_path,developer):

    with open(file_path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        found_developer=False
        print(f'Videogames developed by {developer}:')
        for videogame in reader:
            if videogame['developer'].lower()==developer.lower():
                found_developer=True
                print(f'{videogame['name']}(Classification: {videogame['classification']},Genre: {videogame['genre']})')
                

        if not found_developer:
            print(f'No videogames found for developer {developer}')

def main():
    developer=ask_developer()
    file_reader('Ejercicios de manejo de CSV/my_videogames.csv',developer)


if __name__=='__main__':
    main()
