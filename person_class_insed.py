class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


your_name = input("Your Name : ")
your_age = int(input("Your Age : "))
person = Person(your_name, your_age)
person.greet()
