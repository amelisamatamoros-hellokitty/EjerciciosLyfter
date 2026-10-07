class Bus:
    
    def __init__(self,max_passengers):
        self.max_passengers=max_passengers
        self.passengers=[]

    def add_passengers(self,person):
        if len(self.passengers)<self.max_passengers:
            self.passengers.append(person)
            print(f"Passenger {person.name} added succesfully")
        else:
            print("The bus has exceeded the max number of allowed passengers, remove passengers to add new ones if needed")

    def remove_passengers(self,person):
        for passenger in self.passengers:
            if passenger.name.lower()==person.name.lower():
                self.passengers.remove(passenger)
                print(f"Passenger {passenger.name} was removed successfully")
                break
        else:
            print(f"Passenger {person.name} is not in the bus")

        

class Person:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return f"{self.name!r}"


bus_1=Bus(int(input("Enter the max number of passengers allowed in the bus: ")))
counter=0
while counter < bus_1.max_passengers:
    person_name=Person(input("Enter the name of the person you want to add to the bus:   "))
    bus_1.add_passengers(person_name)
    counter+=1

remove_person=input("Do you want to remove a passenger from the bus?(y/n) ")
if remove_person.lower()=="y":
    person_name=Person(input("Enter the name of the person you want to remove from the bus:   "))
    bus_1.remove_passengers(person_name)
else:
    print("No passenger was removed from the bus")    
    
    











