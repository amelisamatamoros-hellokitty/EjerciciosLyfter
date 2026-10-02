

def show_menu():
    print("""Welcome to the Student Control System

1. Add Student
2. View all students
3. View top 3 students by average grade
4. View overall average grade
5. Export data to CSV
6. Import Student data from a CSV
7. Delete a student
8. View failing students
9. Exit""") 


def validate_number():
    while True:
        try:
            menu_option=int(input("Please select an option from the menu above:  "))
            if menu_option <1 or menu_option>9:
                raise KeyError
        except KeyError as e:
            print("Submitted option is not available in the menu")
        except ValueError:
            print("The submitted option is not a valid number")    
        else:
            return menu_option



        