
from menu import show_menu, validate_number
from actions import Student,add_student,view_students,top_3_averages,average_grades,delete_student,failed_students, exit_program
from data import export_data, import_data



def menu_action():
    student_list=[]
    while True:
        show_menu()
        menu_option=validate_number()
        if menu_option==9:
            exit_program()
            break
        if menu_option==6:
            student_list=import_data(student_list)
        elif menu_option==1:
            student_list=add_student(student_list)        
        try:
            if menu_option==2:
                view_students(student_list)
            elif menu_option==3:
                top_3_averages(student_list)
            elif menu_option==4:
                average_grades(student_list)
            elif menu_option==5:
                export_data(student_list)
            elif menu_option==7:
                delete_student(student_list)
            elif menu_option==8:
                failed_students(student_list)
        except UnboundLocalError as e:
            print ('You have to submit a list of students to access this option, submit a student list with option 1 or 6')

starting_point=menu_action()