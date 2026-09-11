print("----analysis of your grades----")
total_grades=int(input("Enter the total number of grades you want to analyze: "))
grade_counter=1
approved_grades=0
failed_grades=0
approved_total=0
failed_total=0
total_average=0
while grade_counter<=total_grades:
    print(f"please enter the grade number {grade_counter}")
    grade=float(input())
    if grade<=70:
        failed_grades=failed_grades + 1
        failed_total=failed_total + grade
    else:
        approved_grades=approved_grades+1
        approved_total=approved_total+grade
    grade_counter=grade_counter+1
total_average=(failed_total+approved_total)/total_grades
if approved_grades!=0:
    approved_average=approved_total/approved_grades
else:
    approved_average=0
if failed_grades!=0:
    failed_average=failed_total/failed_grades
else:
    failed_average=0
print(f"the number of approved grades is: {approved_grades}")
print(f"the number of failed grades is: {failed_grades}")
print(f"the average of all your grades is: {total_average}")
print(f"Your approved grades average is: {approved_average}")
print(f"Your failed grades average is: {failed_average}")

