class Person:
    def __init__(self, name, age, address, phone_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

    
    def update_contact_info(self, new_address, new_phone_number):
        self.address = new_address
        self.phone_number = new_phone_number

   
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

your_name = input("Your Name : ")
your_age = int(input("Your Age : "))
your_add = input("Your Address : ")
your_ph  = int(input("Your Ph : "))

person = Person(your_name, your_age, your_add, your_ph)  # Replace with actual details

person.display_info()

your_add_update = input("Your New Address : ")
your_ph_update  = int(input("Your New ph : "))

person.update_contact_info(your_add_update, your_ph_update)

person.display_info()
