def word_counter(path):
    with open(path,'r',encoding="utf-8") as file:
        lines=file.read()
        result=len(lines.split())
    return result
            

my_file='Ejercicios extra manejo de archivos/hello_world.txt'
final_result=word_counter(my_file)
print(f'This archive contains {final_result} words')

