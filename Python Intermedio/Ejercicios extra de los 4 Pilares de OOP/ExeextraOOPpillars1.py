class Employee:
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if any(c.isdigit()for c in value)==True:
            raise ValueError("The name can't contain numbers")
        self._name=value

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if value<0:
            raise ValueError("Salary can't be negative")
        self._salary=value

    def promote(self,salary_raise):
        self.salary=self.salary*(1+salary_raise)
        return self.salary


try:
    employee=Employee("Ana",1000)
except ValueError as e:
    print(e)

try:
    employee.promote(0.1)
    print(employee.salary)
except NameError as e:
    print("Invalid name and/or salary, promotion can't be calculated")    
