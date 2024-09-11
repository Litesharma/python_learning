'''
private (like) attributes & method
conceptiual implementation in python

they are meant to be used only within the class and are not accessible from outside the class

'''
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age              # make it private
# print(Student("sahil","15").name)
# print(Student("sahil","15").age) # it gives an error because it is private now


'''
inheritance : parent se child me properties ko inherit karna
'''

# class Car:
#     @staticmethod
#     def start():
#         print("car started ")
#     @staticmethod
#     def stop():
#         print("car stop ")
# # Single inheritance: NewCar inherits from Car
# class NewCar(Car):
#     def __init__(self,brand):               
#         self.brand=brand
# # Multi-level inheritance: CarModel inherits from NewCar, which inherits from Car
# class CarModel(NewCar):
#     def __init__(self,model):
#         self.model=model

# c=CarModel("320B4U")
# print(c.model)
# c.start()
# c.stop()

'''
Multiple inheritance 
'''
# class A:
#     varA="welcome A "
# class B:
#     varB="welcome B "
# class C(A,B):
#     varC="welcome C "
# c1=C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)


'''
super() method: it is used to access the methods of the parent class

'''
# class Car:
#     def __init__(self,color):
#         self.color=color
#     @staticmethod
#     def start():
#         print("car started ")
#     @staticmethod
#     def stop():
#         print("car stop ")

# class NewCar(Car):
#     def __init__(self,brand,color):               
#         super().__init__(color)
#         self.brand=brand

# class CarModel(NewCar):
#     def __init__(self,model,brand,color):
#         super().__init__(brand,color)
#         self.model=model

# c=CarModel("320B4U","BMW","green")
# print(c.model)
# print(c.brand)
# print(c.color)

# #print(c.brand)   now here i want to access the brand name but i can't so i will use super() method
# c.start()
# c.stop()


'''
Class method : it helps to change the class attributes in methods 

'''
# class person:
#     name="bhola"
#     def changeName(self,name):
#         # self.name=name                  # this will not change the class's name
#         # person.name=name                # this will change the name 
#         # self.__class__.name=name        # this will change the name
# p1=person()
# p1.changeName("chintu")
# print(p1.name)
# print(person.name)

# class person:
#     name="bhola"
#     @classmethod              # decorator
#     def changeName(cls,name):
#         cls.name=name

# p1=person()
# p1.changeName("chintu")
# print(p1.name)
# print(person.name)



'''
@property attribute : converts method to attrubute with updated values


'''

# class Table:
#     def __init__(self,n):
#         self.n=n
#         # self.t=n*2                  # now we have changes the value to 5 but it will again print 8
#     @property
#     def t(self):
#         return self.n*2               # now it will return the updated value 10
    
# s=Table(4)
# s.n=5                  
# print(s.t)