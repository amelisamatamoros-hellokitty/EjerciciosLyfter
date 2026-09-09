def song_reader(path):
    with open(path,'r',encoding='utf-8') as file:
        content=file.readlines()
        organized_file=sorted(content)
        final_file=''.join(organized_file)
    return final_file


def new_song_file(path,text):
    with open(path,'w',encoding='utf-8') as file:
        file.write(text)
    return text

original_list='Ejercicios Manejo de Archivos/songs.txt'
new_list='Ejercicios Manejo de Archivos/new_file.txt'

songs=song_reader(original_list)
final_file=new_song_file(new_list,songs)
print(final_file)