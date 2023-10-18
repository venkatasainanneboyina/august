
print ('1.SINGLE INHERITENCE.')
# Parent class (base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class (derived class) inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Child class (derived class) inheriting from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

# Create instances of the child classes
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

# Call the speak method on instances of the child classes
dog.speak()  # Outputs: "Buddy barks"
cat.speak()  # Outputs: "Whiskers meows"

print ('2.MULTIPLE INHERITENCE.')
# Parent class 1
class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} chirps")

# Parent class 2
class Mammal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a generic mammal sound")

# Child class inheriting from Bird and Mammal
class Bat(Bird, Mammal):
    def fly(self):
        print(f"{self.name} can fly")

# Create an instance of the Bat class
bat = Bat("Batty")

# Call the speak method and the fly method
bat.speak()  # Outputs: "Batty chirps"
bat.fly()    # Outputs: "Batty can fly"

print ('3.Mutilevel inheritence.')
# Grandparent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Parent class inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

# Child class inheriting from Student
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, graduation_year):
        super().__init__(name, age, student_id)
        self.graduation_year = graduation_year

    def display_info(self):
        super().display_info()
        print(f"Graduation Year: {self.graduation_year}")

# Create an instance of the GraduateStudent class
graduate_student = GraduateStudent("vicky", 25, "12345", 2024)

# Call the display_info method
graduate_student.display_info()

print('4.Hierarichical inheritence')
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Child class 1 inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Child class 2 inheriting from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

# Child class 3 inheriting from Animal
class Cow(Animal):
    def speak(self):
        print(f"{self.name} moos")

# Create instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Call the speak method on instances of the child classes
dog.speak()  # Outputs: "Buddy barks"
cat.speak()  # Outputs: "Whiskers meows"
cow.speak()  # Outputs: "Bessie moos"





