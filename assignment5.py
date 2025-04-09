ASSIGNMENT1

# Base class for Superhero
class Superhero:
    # Constructor to initialize superhero attributes
    def __init__(self, name, power, city, secret_identity):
        self.name = name
        self.power = power
        self.city = city
        self.secret_identity = secret_identity

    # Method to display superhero details
    def display_details(self):
        return f"Superhero: {self.name}, Power: {self.power}, City: {self.city}, Secret Identity: {self.secret_identity}"
    
    # Method for superhero action
    def fight_crime(self):
        return f"{self.name} is fighting crime in {self.city} using {self.power}!"

# Derived class for a specific type of Superhero, like a "FlyingHero"
class FlyingHero(Superhero):
    def __init__(self, name, power, city, secret_identity, flying_speed):
        # Call to the base class constructor
        super().__init__(name, power, city, secret_identity)
        self.flying_speed = flying_speed
    
    # Overriding the fight_crime method to demonstrate polymorphism
    def fight_crime(self):
        return f"{self.name} is flying at {self.flying_speed} km/h to fight crime!"

# Create an instance of Superhero
hero1 = Superhero("Captain Justice", "Super Strength", "Metropolis", "John Doe")
print(hero1.display_details())  # Output hero details
print(hero1.fight_crime())  # Hero action

# Create an instance of FlyingHero
hero2 = FlyingHero("Sky Flyer", "Flight", "Gotham", "Jane Smith", 1200)
print(hero2.display_details())  # Output hero details
print(hero2.fight_crime())  # Hero action with flying speed


ACTIVITY2

# Base class for Animal
class Animal:
    def move(self):
        pass

# Dog class that inherits Animal
class Dog(Animal):
    def move(self):
        return "The dog is running "

# Cat class that inherits Animal
class Cat(Animal):
    def move(self):
        return "The cat is walking gracefully "

# Bird class that inherits Animal
class Bird(Animal):
    def move(self):
        return "The bird is flying high "

# Creating instances of each animal and calling move()
animals = [Dog(), Cat(), Bird()]

# Polymorphism in action
for animal in animals:
    print(animal.move())