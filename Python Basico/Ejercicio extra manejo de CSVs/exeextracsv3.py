import csv

def file_reader(file_path):

    with open(file_path,'r',encoding='utf-8',newline='') as file:
        genre_counter={}
        reader=csv.DictReader(file)
        for series in reader:
            series_genre=series['genre']
            genre_counter[series_genre]=genre_counter.get(series_genre,0)+1
    return genre_counter
    
def print_file(dict):
    print('Genres found:')
    for genre,count in dict.items():
        print(f'{genre}: {count}')



def main():
    file='Ejercicios de manejo de CSV/my_videogames.csv'
    my_file=file_reader(file)
    print_file(my_file)

if __name__=='__main__':
    main()
