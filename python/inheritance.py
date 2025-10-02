#polymorphism inhertence
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

dog = Dog("Rocky")
cat = Cat("Sunny")

print(dog.speak())
print(cat.speak())

#super()
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    def speak(self):
        return f"{self.name}, the {self.breed}, barks."

dog = Dog("rocky", "Dog", "Golden Retriever")


print(f"Name: {dog.name}")
print(f"Species: {dog.species}")
print(f"Breed: {dog.breed}")
print(f"Sound: {dog.speak()}")

#multiple
class Animal:
    def speak(self):
        return "Animal sound"
class Vehicle:
    def move(self): 
        return "Moves on the road"
class RobotDog(Animal, Vehicle):
    def speak(self): 
        return "RobotDog barks electronically"
robot_dog = RobotDog()

print(f"Speak method: {robot_dog.speak()}") 
print(f"Move method: {robot_dog.move()}")   

