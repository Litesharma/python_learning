# def greet(n):
#     print(f"good morning ... {n}")

# n=input("enter your name : ")
# a=5
# b=6
# print(__name__)
# greet(n)

'''keyword argument'''

# def sup(a,b,c=9):
#     return a+b+c
# print(sup(b=5,a=9,c=8))

'''returning multiple values'''

# def yo(a,b,c):
#     return a*b,b*c,c*a
# t=yo(2,3,4)
# print(t)                     # always return a tuple when multiple return statements used
# print(type(t))
# a,b,c=yo(2,3,4)
# print(a,b,c,sep=" ")
# print(type(a))

'''global and local variable '''

# life time of variable --> it is time for which a variable lives in a memory
# for Global var --> the lifetime is the entire program run i.e they live in program as long as the program is running )
# for local var--> lofe time is their function's run 



'''
Name resolution (Resolving scope of a Name )
when we access any variable from within a program or funciton, python follows name resolution rule

known as "LEGB" Rule 
i.) it checks in "local environment" if not then moves to next step
ii.) now python cheks in "Enclosing environment" if not then moves to next step
iii.) now it cheks in "Global env"
iv.) now it checks in "built in variable " if not present python returns an error < variable not found>
'''


# same variable name in global scope as well as in local scope 

# if this happens python will create the variable in local environment 

# def state():
#     tiger=15
#     print(tiger)

# tiger=95
# print(tiger)
# state()
# print(tiger)

# if want to use the global variable in local variable we have to add a global statement before tiger
# def state():
#     global tiger
#     print(tiger)
# print("new")
# tiger=95
# print(tiger)
# state()
# print(tiger)

'''passing a mutable tupe value to a function making changes in place'''

# def l(myList):
#     myList[0]+=2

# list=[1,2]
# print(list)
# l(list)                 # list is mutable so it changes 
# print(list)

