class Car:
    def drive(this):
        print("wroom wroom")
    
bmw = Car()
bmw.drive()

#----------------inheritance
class Animal:
    def speak(this):
        print("speaking")

class MiniPig(Animal):
    def speak(this):
        print("weee-weeee")

class Dog(Animal):
    def speak(this):
        print("voof-voof")

pig = MiniPig()
pig.speak()

dog = Dog()
dog.speak()

myAnimals = [MiniPig(), Dog()]

for item in myAnimals:
    item.speak()

def talk(obj):
    obj.speak()

talk(MiniPig())
#------------------------------конструктор

class Student:
    def __init__(self,name):
        self.name = name
        self._age = 20
        self.__hobby = "Polo"
    def __str__(self):
        return f"Name: {self.name} Age: {self._age}"
    
    def get_hobby(self):
        return self.__hobby


ivan = Student("ivan")
print("name: ", ivan.name)
print("age: ", ivan._age)
print(ivan.get_hobby())
print(ivan)