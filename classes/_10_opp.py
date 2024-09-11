'''
classes: classes are like a blueprint for creating objects(instance)
'''
# class Student:
#     name="billu"

# s1=Student()
# print(s1)                # memory location and type(object) will print
# print(s1.name)           # name(billu) will print

'''
constructer: all classes have a function called __init__ which run every time when a object is created 
and it is known as constructer

self: it is a reference to the current object(instance)
attributes: these are the variables inside the class that store the information about an object
'''
# class Student:
#     def __init__(self):        # self is a refernce to the current instance i.e s1
#         print(self)
#         print("hey you are in construcor")

# s1=Student()             # now object s1 is created then constructor is called ; morover, () is used to call that 

# class Student:
#     def __init__(self,fullname,marks):
#         self.name=fullname             # self.name is an isntance attribute full name is a parameter
#         self.marks=marks
# s1=Student('billu',52)
# print(s1.name)
# print(s1.marks)

'''
Create a class named Laptop.
Add an instance attribute for brand and price using the constructor (__init__).
Add a class attribute for category with the value "Electronics".
Create two objects of Laptop with different brand and price values.
Print the brand, price, and category for both objects.
'''
# creating class
# class Laptop:
#     category="Electronics"             # class attribute
#     def __init__(self,brand,prize):
#         self.brand=brand               # instance attribute
#         self.prize=prize               # instance attribute

# # creating object
# l1=Laptop('lenovo','49k')
# l2=Laptop('honor','42k')

# print(f'category : {l1.category}')
# print(f"laptop 1\nbrand:{l1.brand}\nprize:{l1.prize}")
# print(f"laptop 2\nbrand:{l2.brand}\nprize:{l2.prize}")

