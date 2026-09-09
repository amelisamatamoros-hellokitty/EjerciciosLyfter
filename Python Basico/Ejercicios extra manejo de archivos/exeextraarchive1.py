def text_reader(path):
    with open(path,'r',encoding='utf-8') as file:
        lines=file.read()
        clean_file=lines.replace('\n',' ')
    return clean_file

def file_creator(path,text):
    with open(path,'w',encoding='utf-8') as file:
        new_file=file.write(text)
    return new_file

hi_world='Ejercicios extra manejo de archivos/hi_world.txt'
hello_world='Ejercicios extra manejo de archivos/hello_world.txt'

fixed_file=text_reader(hi_world)
file_creator(hello_world,fixed_file)
