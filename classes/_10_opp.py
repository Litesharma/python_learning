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

'''methods : methods are the functions that belongs to 
the class and interacts with the instance(object)'s attribute'''

#create class

# class Student:
#     def __init__(self,name,age):         # paramirized constructor i.e a constructor having parameters
#         self.name=name
#         self.age=age
#     def hello(self):                     # refering current object
#         print(f"hello {self.name} your age is {self.age}\nHappy sunday!!!")

# s=input("Enter your name : ")
# a=int(input("Enter your age : "))

# # create an object 

# s1=Student(s.title(),a)
# s1.hello()


'''
Create a class named Student.
Add attributes name and grade using the constructor.
Add a method show_info() that prints "Name: [name], Grade: [grade]".
Create an object of Student and call show_info()
'''

# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     def show_info(self):
#         print(f'Name : {self.name}\ngrade : {self.grade}')

# s=input("Enter your name : ")
# g=int(input("Enter your grade : "))

# s1=Student(s.title(),g)
# s1.show_info()


'''
class question 1
'''
# class Student:
#     def __init__(self,name,marks1,marks2,marks3) :
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
#     def avg(self):
#         avg=(self.marks1 + self.marks2 + self.marks3)/3
#         print(f"average marks is {avg}")

# s=input("Enter your name : ")
# marks1=int(input("Enter your marks1 : "))
# marks2=int(input("Enter your marks2 : "))
# marks3=int(input("Enter your marks3 : "))

# s1=Student(s,marks1,marks2,marks3)
# s1.avg()

'''
static method:when we do not want to use self means we do not use objects for that

'''
# class Student:
#     @staticmethod             # decorator : function ke beheviour ko change karte hain
#     def hello():
#         print("hello world")

# s=Student()
# s.hello()


'''
create an account class and add 2 attributes balance and account num 
and create methods to credit , debit and printing the balance 

'''

class Account:
    def __init__(self,balance,accountNum):
        self.balance=balance
        self.accountNum=accountNum
    
    def credit(self,creditAmount):
        self.balance+=creditAmount
        print(f"{creditAmount} is credited in your account {self.accountNum}\nTotal availiable balance is {self.balance} ")
    def debit(self,debitAmount):
        self.balance-=debitAmount
        print(f"{debitAmount} is debited from your account {self.accountNum}\nTotal availiable balance is {self.balance} ")
    def checkBal(self):
        print(f"Total available balance is {self.balance}")
        
balance = float(input("Enter your total balance: "))
accountNum = int(input("Enter your account number: "))

user=Account(balance,accountNum)
user.debit(2000)