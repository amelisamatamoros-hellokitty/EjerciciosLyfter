class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Makes a sound")

class Dog(Animal):
    def speak(self):
        print("Guau")

class Cat(Animal):
    def speak(self):
        print("Miau")

dog=Dog("Martina")
dog.speak()

cat=Cat("Pandora")
cat.speak()
