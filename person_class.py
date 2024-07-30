class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

your_name = input("Your Name : ")
your_age = int(input("Your Age : "))
person = Person(your_name, your_age) 

# Print the object's attributes
print(f"Name: {person.name}")
print(f"Age: {person.age}")
