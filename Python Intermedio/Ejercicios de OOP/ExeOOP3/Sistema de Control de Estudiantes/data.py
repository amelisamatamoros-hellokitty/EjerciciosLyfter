import csv
from actions import Student

def export_data(student_list):
    data=[]
    file_path=input('Submit the name for the csv file you want to create: ')
    for student in student_list:
        dict_stud={}
        dict_stud['name']=student.name
        dict_stud['section']=student.section
        dict_stud['spanish_note']=student.spanish_note
        dict_stud['english_note']=student.english_note
        dict_stud['socials_note']=student.socials_note
        dict_stud['science_note']=student.science_note
        data.append(dict_stud)
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
            for student in reader:
                name=student['name']
                section=student['section']
                spanish_note=int(student['spanish_note'])
                english_note=int(student['english_note'])
                socials_note=int(student['socials_note'])
                science_note=int(student['science_note'])
                student_list.append(Student(name,section,spanish_note, english_note, socials_note, science_note))
        return student_list
    except FileNotFoundError as e:
        print('The submitted file name has not been exported, import data first to a csv file ')

