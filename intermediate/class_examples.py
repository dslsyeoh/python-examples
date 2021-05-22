class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Bob", 30)
person2 = Person("John", 40)

print(f"name: {person.name} age: {person.age}")
print(f"name: {person2.name} age: {person2.age}")

del person2

person.name = "Max"

print(f"name: {person.name} age: {person.age}")
