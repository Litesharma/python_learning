'''
question 1 
'''

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         a=3.14*self.radius**2
#         print(f'area of circle is {a}\n')
#     def perim(self):
#         p=2*3.14*self.radius
#         print(f'perimeter of circle is {p}\n')

# r=int(input("Enter radius of circle : "))
# c=Circle(r)
# c.area()
# c.perim()

'''
Quesion : 2

'''
# class Employe:
#     def __init__(self,attr_role,dept,salry):
#         self.attr_role=attr_role
#         self.dept=dept
#         self.salry=salry
#     def show_details(self):
#         print(f'Attribute Role : {self.attr_role}\nDepartment : {self.dept}\nSalary : {self.salry}')

# class Engineer(Employe):
#     def __init__(self,name,age,attr_role,dept,salry):
#         super().__init__(attr_role,dept,salry)
#         self.name=name
#         self.age=age
#     def show_details(self):
#         super().show_details()
#         print(f"name : {self.name}\nage: {self.age}")

# e1=Engineer("Raju",21,"Data Engineer","Swe",15000)
# e1.show_details()

        

'''
Question :>3

'''

class Order:
    def __init__(self,item,pris):
        self.item=item
        self.pris=pris

    def __gt__(self,o2):
        order1=self.pris
        order2=o2.pris
        return order1>order2
    

o1=Order("Milk",1000)
o2=Order("Oil",1000)
if(o1>o2):
    print(f"prize of {o1.item} is greater then {o2.item}")
elif(o1.pris==o2.pris):
    print(f"prize of {o2.item} is equal to {o1.item}")
else:
    print(f"prize of {o2.item} is greater then {o1.item}")

