class Person:

    def __init__(self, name, age, address, phone_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number


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

class Student(Person):

    def __init__(self, name, age, address, phone_number, student_id):
        super().__init__(name, age, address, phone_number)
        self.student_id = student_id


    def display_info(self):
        super().display_info() 
        print(f"Student ID: {self.student_id}")

your_name = input("Your Name : ")
your_age = int(input("Your Age : "))
your_add = input("Your Address : ")
your_ph  = int(input("Your Ph : "))
your_id  = int(input("Your Student ID : "))
student = Student(your_name, your_age, your_add, your_ph,  your_id)  
student.display_info()
