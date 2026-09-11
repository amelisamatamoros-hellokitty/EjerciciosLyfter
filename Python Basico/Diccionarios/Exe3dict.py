list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
for item in list_of_keys:
        if item in employee:
            employee.pop(item)
print(employee)

