class Person:
    def __init__(self, unique_id, name, age, city, gender):
        self.unique_id = unique_id
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender

    def eats(self):
        return f"{self.name} is eating."

    def study(self):
        return f"{self.name} is studying."

    def sleep(self):
        return f"{self.name} is sleeping."

    def play(self):
        return f"{self.name} is playing."

# Instances
John = Person(unique_id=1, name="John", age=35, city="Delhi", gender="male")
Dessy = Person(unique_id=2, name="Dessy", age=20, city="Pune", gender="female")

# Output
print("John's Information:")
print("ID:", John.unique_id)
print("Name:", John.name)
print("Age:", John.age)
print("City:", John.city)
print("Gender:", John.gender)
print(John.eats())
print(John.study())
print(John.sleep())
print(John.play())

print("\nDessy's Information:")
print("ID:", Dessy.unique_id)
print("Name:", Dessy.name)
print("Age:", Dessy.age)
print("City:", Dessy.city)
print("Gender:", Dessy.gender)
print(Dessy.eats())
print(Dessy.study())
print(Dessy.sleep())
print(Dessy.play())
