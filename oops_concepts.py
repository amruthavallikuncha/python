
# Class definition - Basic OOP Concepts
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

# Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # Calling the constructor of the parent class
        self.breed = breed

    # Overriding the make_sound method
    def make_sound(self):
        print(f"{self.name} barks loudly!")

# Encapsulation
class Car:
    def __init__(self, brand, model):
        self._brand = brand  # Protected attribute
        self.__model = model  # Private attribute

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        if isinstance(new_model, str):
            self.__model = new_model
        else:
            print("Invalid model type!")

# Polymorphism
def make_animal_sound(animal_obj):
    animal_obj.make_sound()

# Creating instances
cat = Animal("Whiskers", "Meow")
german_shepherd = Dog("Buddy", "German Shepherd")
my_car = Car("Toyota", "Camry")

# Using encapsulation
model_of_car = my_car.get_model()
print(f"Model of the car: {model_of_car}")

# Modifying model using the setter
my_car.set_model("Corolla")

# Using polymorphism
make_animal_sound(cat)
make_animal_sound(german_shepherd)
