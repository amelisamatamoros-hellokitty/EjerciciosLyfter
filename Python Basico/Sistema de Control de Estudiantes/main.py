
from menu import show_menu, validate_number
from actions import menu_option1,menu_option2, menu_option3, menu_option4, menu_option7, menu_option8, menu_option9
from data import menu_option5, menu_option6



def menu_action():
    while True:
        show_menu()
        menu_option=validate_number()
        if menu_option==9:
            menu_option9()
            break
        if menu_option==6:
            student_list=menu_option6()
        elif menu_option==1:
            student_list=menu_option1()        
        try:
            if menu_option==2:
                menu_option2(student_list)
            elif menu_option==3:
                menu_option3(student_list)
            elif menu_option==4:
                menu_option4(student_list)
            elif menu_option==5:
                menu_option5(student_list)
            elif menu_option==7:
                menu_option7(student_list)
            elif menu_option==8:
                menu_option8(student_list)
        except UnboundLocalError as e:
            print ('You have to submit a list of students to access this option, submit a student list with option 1 or 6')

starting_point=menu_action()