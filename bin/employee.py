import random

class Employee:

    list_of_employees = {'1':'Neha', '2':'Sabah', '3':'Maggi'}

    def __init__(self):
         random_employee = random.sample(self.list_of_employees,1)
         self.id = random_employee[0]
         self.name = self.list_of_employees[random_employee[0]]


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name