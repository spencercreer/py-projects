"""
Four Pillars of Object-Oriented Programming
1) Abstraction
2) Inheritance
3) Encapsulation
4) Polymorphism
"""

class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I'm a teacher")

class Customer(User):
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def update_membership(self, new_membership):
        print("Calculating cost of new membership")
        self.membership = new_membership

    def read_customer():
        print("Reading customer from DB")

    def __str__(self):
        print("Converting to string")
        return self.name + " " + self.membership

    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    
    def __eq__(self, other):
        if self.name == other.name and self.membership == other.membership:
            return True
        return False

    __hash__ = None

    __repr__ = __str__

customers = [Customer("Caleb", "Gold"), Customer("Brad", "Bronze"), Customer("Caleb", "Gold")]

print(customers[1])
customers[1].update_membership("Gold")
print(customers[1].membership)

Customer.read_customer()

Customer.print_all_customers(customers)

print(customers[0] == customers[2])
print(id(customers[0]), id(customers[2]))

customers[0].log()

users = [Customer("Caleb", "Gold"), Customer("Brad", "Bronze"), Customer("Caleb", "Gold"), Teacher()]


for user in users:
    user.log()