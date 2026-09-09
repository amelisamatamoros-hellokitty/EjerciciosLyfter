def add_text(path,text):
    with open(path,'a',encoding="utf-8") as file:
        content=file.write("\n"+text)
    return content

new_text=input('Please enter a text you want to add:')
my_file='Ejercicios extra manejo de archivos/hello_world.txt'
add_text(my_file,new_text)


