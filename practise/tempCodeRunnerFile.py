'''
Quesion : 2

'''
class Employe:
    def __init__(self,attr_role,dept,salry):
        self.attr_role=attr_role
        self.dept=dept
        self.salry=salry
    def show_details(self):
        print(f'Attribute Role : {self.attr_role}\nDepartment : {self.dept}\nSalary : {self.salry}')

class Engineer(Employe):