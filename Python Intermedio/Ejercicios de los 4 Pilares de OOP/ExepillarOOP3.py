#Herencia múltiple es cuando una clase hereda de dos o más clases padre a la vez, 
#y recibe los métodos y atributos de todas ellas.

class Person:

    def __init__(self,name,id,**kwargs):
        super().__init__(**kwargs)
        self.name=name
        self.id=id

    def present(self):
        print(f"I am {self.name}, ID {self.id} ")

    def define_role(self):
        pass

class Doctor(Person):

    def __init__(self,specialty, college_number,**kwargs):
        super().__init__(**kwargs)
        self.specialty=specialty
        self.college_number=college_number
        

    def diagnose(self,patient, disease):
        print(f"The doctor determined that {patient} had {disease}")

    def define_role(self):
        super().define_role()
        print(f"Doctor with college number {self.college_number} and {self.specialty}")


class Investigator(Person):

    def __init__(self,study_field,**kwargs):
        super().__init__(**kwargs)
        self.study_field=study_field

    def publish_article(self,title):
        print(f"Dr. {self.name} published {title} in {self.study_field}")


    def define_role(self):
        super().define_role()
        print(f"Investigator in {self.study_field}")



class MedicalInvestigator(Doctor,Investigator):

    def __init__(self, hrs_clinic,hrs_investigation,**kwargs):
        super().__init__(**kwargs)
        self.hrs_clinic=hrs_clinic
        self.hrs_investigation=hrs_investigation


    def describe(self):
        super().present()
        super().define_role()
        print(f"Clinic hours: {self.hrs_clinic}, investigation hours: {self.hrs_investigation}")

m=MedicalInvestigator(name="Marta", id=5687, specialty="Pediatrician", college_number=56101, study_field="Genetics",
hrs_clinic=450,hrs_investigation=200)

m.describe()