def uppercase_converter(path):
    with open(path,'r',encoding='utf-8') as file:
        content=file.read()
        result=content.upper()
    return result

def new_archive_creator(path,text):
    with open(path,'w',encoding="utf-8") as file:
        content=file.write(text)
    return content

my_file='Ejercicios extra manejo de archivos/hi_world.txt'
first_file=uppercase_converter(my_file)
final_file=new_archive_creator("new_archive.txt",first_file)