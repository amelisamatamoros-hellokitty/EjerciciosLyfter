import csv

def file_creator(file_path):
    with open(file_path,'r',encoding='utf-8',newline='') as file:
        reader=csv.reader(file)
        header=next(reader)
        for line in reader:
            print(f"""
                    Name:{line[0]}
                    Genre: {line[1]}
                    Developer: {line[2]}
                    Classification: {line[3]}
                """)

file_creator('Ejercicios de manejo de CSV/my_videogames.csv')
