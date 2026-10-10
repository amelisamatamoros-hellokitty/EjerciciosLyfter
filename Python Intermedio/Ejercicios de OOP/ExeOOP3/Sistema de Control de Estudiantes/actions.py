import re

class Student:
    def __init__(self,name,section,spanish_note, english_note, socials_note, science_note):
        self.name=name
        self.section=section
        self.spanish_note=spanish_note
        self.english_note=english_note
        self.socials_note=socials_note
        self.science_note=science_note

    
def invalid_name(name):
    valid_name=any(character.isdigit() for character in name) or name==''or name.isspace()
    return valid_name


def is_valid_section(section):
    pattern = r'^\d{2}[A-Za-z]$'
    return bool(re.match(pattern, section))


def student_exists(student_list,student_name,student_section):
    for student in student_list:
        if student.name==student_name and student.section==student_section:
            return True
    else:
        return False

    

def add_student(student_list):  

    while True:
        try:
            student_number=int(input("How many students you want to submit?  "))
            if student_number>0:
                break
            elif student_number<=0:
                raise UnboundLocalError
        except UnboundLocalError as e:
            print('The submitted option is invalid, submit a number starting from 1')
        except ValueError as e:
            print('The submitted option is not a number, submit a number starting from 1')


    for index in range (1, student_number+1):
        while True:
            while True:
                try:    
                    name=input(f"Submit student no. {index}'s complete name   ")
                    student_name=invalid_name(name)
                    if student_name==False:
                        break
                    else:
                        raise ValueError
                except ValueError as e:
                    print("The name shouldn't contain numbers or empty spaces")

            while True:
                try:
                    section=input(f"Submit student no. {index}'s section.  ")
                    student_section=is_valid_section(section)
                    if student_section==True:
                        break
                    else:
                        raise ValueError 
                except ValueError as e:
                    print('The submitted section is incorrect, write again the section with the correct format, a 2-digit number and a letter')
        
            student_verification=student_exists(student_list,name,section)
            if student_verification==False:
                break
            else:
                print('The submitted student already exists, proceed to type another student')

        
        while True:
            try:
                spanish_note=int(input(f"Submit student no. {index}'s spanish note.  "))
            except ValueError:
                print('The submitted information is not a number, please try again')
                continue
            if spanish_note< 0 or spanish_note>100:
                print('Note must be between 0 and 100, please submit the spanish note again')
            else:
                break
        
        while True:
            try:       
                english_note=int(input(f"Submit student no. {index}'s english note  "))
            except ValueError:
                print('The submitted information is not a number, please try again')
                continue
            if english_note< 0 or english_note>100:
                print('Note must be between 0 and 100, please submit the english note again')
            else:
                break
        
        while True:
            try:
                socials_note=int(input(f"Submit student no. {index}'s socials note  "))
            except ValueError:
                print('The submitted information is not a number, please try again')
                continue
            if socials_note< 0 or socials_note>100:
                print('Note must be between 0 and 100, please submit the socials note again')
            else:
                break            
        
        while True:
            try:            
                science_note=int(input(f"Submit student no. {index}'s science note  "))
            except ValueError:
                print('The submitted information is not a number, please try again')
                continue         
            if science_note< 0 or science_note>100:
                print('Note must be between 0 and 100, please submit the science note again')
            else:
                break        
        
        student_list.append(Student(name,section,spanish_note, english_note, socials_note, science_note))
    return student_list  


def view_students(student_list):
    if student_list==[]:
        print('Your student list is empty, we can not action this option')
    else:
        print(f'this is the list of students in your control system:')
        for student in student_list:
            print(f'Name: {student.name}, Section: {student.section}, Spanish note: {student.spanish_note}, English note: {student.english_note}, Socials Note: {student.socials_note}, Science Note:{student.science_note}')
    
def top_3_averages(student_list):
    average_list={}
    for student in student_list:
        average_list[student.name+ "-"+ student.section]=(int(student.spanish_note)+int(student.english_note)+int(student.socials_note)+int(student.science_note))/4
    top_3_students=sorted(average_list.items(),key=lambda x: x[1], reverse=True)[:3]    
    print('The top three student averages are: ')
    for name,average in top_3_students:
        print(name, average)

    
def average_grades(student_list):
    average_list={}
    for student in student_list:
        average_list[student.name+ "-"+ student.section]=(int(student.spanish_note)+int(student.english_note)+int(student.socials_note)+int(student.science_note))/4
    print("All student's averages are: ")
    for name,average in average_list.items():
        print(name, average)

            
def delete_student(student_list):
    student_to_erase=input("What is the name of the person you want to delete? ")
    student_section=input("What is the section of the person you want to delete? ")
    for student in student_list:
        if student.name.lower().strip()==student_to_erase.lower().strip() and student.section.lower().strip()==student_section.lower().strip():
            while True:
                try:    
                    remove_decision=input(f"A record was found for {student.name} and {student.section}, please confirm you want to remove it (y/n).  ")
                    if remove_decision=='y' or remove_decision=='n':
                        break
                    else:
                        raise ValueError
                except ValueError as e:
                    print('Invalid response, please submit y or n')
            if remove_decision.lower().strip()=='y':
                student_list.remove(student)
                print(f'Student {student.name} was deleted from the control system')
                
                break
            elif remove_decision.lower().strip()=='n':
                print('No futher action for this student')
                break
    else:
        print(f"Student {student_to_erase} was not found in the Control System")            

    
def failed_students(student_list):
    for student in student_list:
        if int(student.spanish_note)<60:
            print(f'{student.name} from section {student.section} failed the Spanish class with {student.spanish_note}')
        if int(student.english_note)<60:
            print(f'{student.name} from section {student.section} failed the English class with {student.english_note}')
        if int(student.socials_note)<60:
            print(f'{student.name} from section {student.section} failed the Socials class with {student.socials_note}')
        if int(student.science_note)<60:    
            print(f'{student.name} from section {student.section} failed the Science class with {student.science_note}')     

    
def exit_program():
    print("You have exited the Control System, have a good day!")
