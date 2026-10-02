import csv

def export_data(data):
    file_path=input('Submit the name for the csv file you want to create: ')
    with open(file_path,'w',encoding='utf-8',newline='') as file:
        headers=data[0].keys()
        writer=csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"You can see the student's information in the following file: {file_path}")

def import_data(student_list):
    try:
        file_path=input('Please submit the name of the csv file you want to import ')    
        with open(file_path,'r',encoding='utf-8') as file:
            reader=csv.DictReader(file)
            student_list.extend(list(reader))
        return student_list
    except FileNotFoundError as e:
        print('The submitted file name has not been exported, import data first to a csv file ')

