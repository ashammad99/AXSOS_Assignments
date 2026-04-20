class Zoo:
    def __init__(self, zoo_name):
        self.animals = []      # list to store all animals
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all(self):
        # polymorphism: each animal has its own feed() behavior
        for animal in self.animals:
            animal.feed()

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def feed(self):
        # default feeding behavior
        self.health_level += 10
        self.happiness_level += 10

    def display_info(self):
        print(f"Animal: {self.name}, Happiness Level: {self.happiness_level}, Health Level: {self.health_level}")


class Lion(Animal):
    def __init__(self, sound, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.sound = sound

    def feed(self):
        # override (different behavior than base class)
        self.health_level += 5
        self.happiness_level += 11


class Tiger(Animal):
    def __init__(self, speed, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.speed = speed

    def feed(self):
        self.health_level += 5
        self.happiness_level += 20


class Monkey(Animal):
    def __init__(self, favourite_food, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.favourite_food = favourite_food

    def feed(self):
        self.health_level += 1
        self.happiness_level += 2


class Bear(Animal):
    def __init__(self, weight, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.weight = weight   # ⚠️ better naming (was favourite_food)

    def feed(self):
        self.health_level += 11
        self.happiness_level += 13


zoo1 = Zoo("Gaza's Zoo")

lion = Lion('roar', 'Simba', 1, 1, 1)
tiger = Tiger('100km/h', 'Shere Khan', 1, 1, 1)
monkey = Monkey('Banana', 'Gorilla', 1, 1, 1)
bear = Bear('15kgm', 'Black Bear', 1, 1, 1)

zoo1.add_animal(lion)
zoo1.add_animal(tiger)
zoo1.add_animal(monkey)
zoo1.add_animal(bear)

zoo1.feed_all()
zoo1.print_all_info()