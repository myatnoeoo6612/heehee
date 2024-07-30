class Person:

    def __init__(self, name, age, address, phone_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.__salary = None 

    def update_contact_info(self, new_address, new_phone_number):
        self.address = new_address
        self.phone_number = new_phone_number

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.age >= 18:
            print("You are an adult.")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

    # Method to greet
    def greet(self):
        print(f"Hello, my name is {self.name}.")


    def set_salary(self, salary):
        self.__salary = salary


    def get_salary(self):
        return self.__salary


    @staticmethod
    def is_adult(age):
        return age >= 18

your_name = input("Your Name : ")
your_age = int(input("Your Age : "))
your_add = input("Your Address : ")
your_ph  = int(input("Your Ph : "))

person = Person(your_name, your_age, your_add, your_ph)
age_to_check = your_age  
print(f"Is {age_to_check} an adult? {Person.is_adult(age_to_check)}")
