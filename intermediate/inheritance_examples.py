class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}"

    def print(self):
        print(self.__str__())


class Staff(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    def calculate_annual_income(self):
        return self.salary * 12

    def print(self):
        print(f"{super().__str__()}\nJob Title: {self.job_title}\nAnnual Income: {self.calculate_annual_income()}")


print("==========================")
person = Person("John", 30)
person.print()
print("==========================")
staff = Staff("Max", 40, "Farmer", 3000)
staff.print()
print("==========================")
staff2 = Staff("Brian", 25, "Jr Programmer", 2500)
staff2.print()
print("==========================")