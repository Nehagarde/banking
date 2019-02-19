from customer import Customer
from employee import Employee
from random import randint

class BankAccount(Customer, Employee):

    customer_name = ''
    customer_acc_no = None
    assigned_employee_id = None
    acc_balance = 5000


    def __init__(self, name, email, phone):
       Customer.set_name(self,name)
       Customer.set_email(self,email)
       Customer.set_phone(self,phone)
       Employee()
       
    def create_account(self):
        self.customer_name = Customer.get_name(self)
        self.customer_acc_no = self.customer_name[0:2]+str(randint(10000,99999))
        print self.customer_name + ": " + self.customer_acc_no

    def deposit(self, amount):
        self.acc_balance += amount

    def withdraw(self, amount):
        self.acc_balance -= amount

    def get_balance(self):
        print self.acc_balance

b = BankAccount('nnn','ngarde@abcd.com',9538523675)
b.create_account()
b.get_balance()
b.deposit(300)
b.get_balance()
b.withdraw(100)
b.get_balance()