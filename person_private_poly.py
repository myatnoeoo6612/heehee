class Person:
    def __init__(self, name, age, address, phone_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def greet(self):
        return f"Hello, I am {self.name}, a person."

    def update_contact_info(self, new_address, new_phone_number):
        self.address = new_address
        self.phone_number = new_phone_number

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

class Student(Person):
    def greet(self):
        return f"Hello, I am {self.name}, a student."

def introduce(person: Person):
    print(person.greet())

# Input details for Person object
your_name = input("Your Name: ")
your_age = int(input("Your Age: "))
your_add = input("Your Address: ")
your_ph = input("Your Phone Number: ")

person = Person(your_name, your_age, your_add, your_ph)
# person.display_info()


# student_name = input("Student Name: ")
# student_age = int(input("Student Age: "))
# student_add = input("Student Address: ")
# student_ph = input("Student Phone Number: ")

student = Student(your_name, your_age, your_add, your_ph)

# Use introduce function with both Person and Student objects
introduce(person)
introduce(student)
