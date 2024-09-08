'''Write a program to find the greatest of four numbers entered by the user'''
# n1=int(input("Enter num1 : "))
# n2=int(input("Enter num2 : "))
# n3=int(input("Enter num3 : "))
# n4=int(input("Enter num4 : "))

# if(n1>n2 and n1>n3 and n1>n4):
#     print(f'{n1} is largest')
# elif(n2>n1 and n2>n3 and n2>n4):
#     print(f'{n2} is largest')
# elif(n3>n1 and n3>n2 and n3>n4):
#     print(f'{n3} is largest')
# else:
#     print(f'{n4} is largest')


'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user'''



# s1=int(input("Enter marks of sub1 : "))
# s2=int(input("Enter marks of sub2 : "))
# s3=int(input("Enter marks of sub3 : "))

# sum=s1+s2+s3
# total_per=(sum/300)*100
# a=(s1/100)*100
# b=(s2/100)*100
# c=(s3/100)*100
# if((total_per>=40) and (a>33 and b>33 and c>33)):
#     print(f'you are pass')

# else:
#     print(f'you are failed your total marks are :{total_per}')


'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams.'''

# a='Make a lot of money'
# b='buy now'
# c='subscribe this'
# d='click this'

# user=input("enter comment : ")
# if(a in user or b in user or c in user or d in user):
#     print("This comment is a spam please be Alert!!!")

'''Write a program to find whether a given username contains less than 10 
characters or not.
'''

# user=input("enter name : ")
# if(len(user)>10):
#     print("length is less then 10")
# else:
#     print("greater then or equal to 10")    

'''Write a program which finds out whether a given name is present in a list or not'''

# a=["rahul",'mohan',"chintu","chinu"]

# user=input("enter name : ")
# if(user in a):
#     print(f"{user} is present ")
# else:
#     print(f"{user} is not present")


'''Write a program to calculate the grade of a student from his marks from the 
following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => f'''

# marks=int(input("enter your marks : "))
# if(100>marks>=90):
#     print("Grade is \"A\" ")
# if(90>marks>=80):
#     print("Grade is \"B\" ")
# if(80>marks>=70):
#     print("Grade is \"c\" ")
# if(70>marks>=60):
#     print("Grade is \"D\" ")
# if(60>marks>=50):
#     print("Grade is \"E\" ")
# if(marks<50):
#     print("Grade is \"F\" ")

