# Una de las propiedades de las clases es la herencia infinita de clases, podemos extendernos mas alla de una clase "padre"
# a una clase abuelo y asi sucesivamente.

class Animal:
    def breath(self):
        print("Breathing")

class Mamal(Animal):
    def breast_feeding(self):
        print("Breastfeeding babies")

class Dog(Mamal):
    def bark(self):
        print("Guau")

class Cat(Mamal):
    def purr(self):
        print("Miau")

p = Dog()
p.breath()     
p.breast_feeding()    
p.bark()   

m=Cat()
m.breath()    
m.breast_feeding()   
m.purr() 