class Animal:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def isMammal(self):
        pass

    def mate(self):
        pass

class Duck(Animal):
    def __init__(self, age, gender):
        super().__init__(age, gender)
        self.beakColor = "yellow"

    def swim(self):
        print("Duck is swimming")

    def quack(self):
        print("Duck is quacking")

class Fish(Animal):
    def __init__(self, age, gender, sizeInFt, canEat):
        super().__init__(age, gender)
        self.sizeInFt = sizeInFt
        self.canEat = canEat

    def swim(self):
        print("Fish is swimming")

class Zebra(Animal):
    def __init__(self, age, gender, is_wild):
        super().__init__(age, gender)
        self.is_wild = is_wild

    def run(self):
        print("Zebra is running")

# Instances
duck_instance = Duck(age=2, gender="Male")
fish_instance = Fish(age=1, gender="Female", sizeInFt=0.5, canEat=True)
zebra_instance = Zebra(age=3, gender="Female", is_wild=True)

# Output
print("Duck:")
print("Age:", duck_instance.age)
print("Gender:", duck_instance.gender)
print("Beak Color:", duck_instance.beakColor)
duck_instance.swim()
duck_instance.quack()
print()

print("Fish:")
print("Age:", fish_instance.age)
print("Gender:", fish_instance.gender)
print("Size in Feet:", fish_instance.sizeInFt)
print("Can Eat:", fish_instance.canEat)
fish_instance.swim()
print()

print("Zebra:")
print("Age:", zebra_instance.age)
print("Gender:", zebra_instance.gender)
print("Is Wild:", zebra_instance.is_wild)
zebra_instance.run()
