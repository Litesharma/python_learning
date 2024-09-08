'''Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!'''

# dect={
#   "Sapna": "Dream",
#   "Madhur": "Sweet",
#   "Sachcha": "True",
#   "Chandramā": "Moon",
#   "Ujjval": "Bright",
#   "Shanti": "Peace",
#   "Suraj": "Sun",
#   "Gaurav": "Pride",
#   "Anand": "Joy",
#   "Swatantra": "Free"
# }
# user=input("Enter word in hindi :")
# eng=dect.get(user,f"No! word found related to {user}")
# print(eng)

'''Write a program to input eight numbers from the user and display all the unique 
numbers (once).
'''

# s=set()        # empety set
# n1=int(input("Enter number 1 : "))
# s.add(n1)
# n2=int(input("Enter number 2 : "))
# s.add(n2)
# n3=int(input("Enter number 3 : "))
# s.add(n3)
# n4=int(input("Enter number 4 : "))
# s.add(n4)
# n5=int(input("Enter number 5 : "))
# s.add(n5)
# n6=int(input("Enter number 6 : "))
# s.add(n6)
# n7=int(input("Enter number 7 : "))
# s.add(n7)
# n8=int(input("Enter number 8 : "))
# s.add(n8)

# print(f"unique numbers are :--->) {s}")



'''What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))           # lenght is 2 as python consider 20.0=20 as they both are numerically equall


'''Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique'''


# d={}
# name=input("enter name: ")
# lang=(input("enter lang: "))
# d.update({name:lang})
# name=input("enter name: ")
# lang=(input("enter lang: "))
# d.update({name:lang})
# name=input("enter name: ")
# lang=(input("enter lang: "))
# d.update({name:lang})
# name=input("enter name: ")
# lang=(input("enter lang: "))
# d.update({name:lang})

# print(d)


'''Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}'''

s = {8, 7, 12, "Harry", [1,2]}
