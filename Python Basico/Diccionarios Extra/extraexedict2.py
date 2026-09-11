employees=[
    {"name":"Carlos","email":"carlos@empresa.com","department":"Ventas"},
    {"name":"Ana","email":"ana@empresa.com","department":"TI"},
    {"name":"Luis","email":"luis@empresa.com","department":"Ventas"},
    {"name":"Sofia","email":"sofia@empresa.com","department":"RRHH"}
]
employees_by_department={}
for single_employee in employees:
    name=single_employee["name"]
    department=single_employee["department"]
    employees_by_department.setdefault(department, []).append(name)
print(employees_by_department)

