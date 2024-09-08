''' list are mutable i.e we can change the original list but strings are immutable we can't change the original strings''' 

# l=list()  # we can also create empty list like that

'''creating list from strings''' 
# l=list('litesh')
# print(l)

'''creating list from tuples'''

# t=('w','a','t','e','r')
# print(list(t))

'''creating list form keyboard input'''

# l1=list(input("Enter list element: "))
# print(l1)

'''2nd way to input a list is eval(input())'''

# l2=eval(input("enter "))
# print(l2)


#functions in list 

'''index method'''
# l1=[1,5,6,8]
# print(l1.index(8))

''' append method'''
# l1=[1,5,6,8]
# t=[2,4]   #it consider this list as whole element
# l1.append(t)   #add 6 at the end and return none
# print(l1)

''' extend method'''
# l1=[1,5,6,8]
# t=[2,4]
# l1.extend(t)    #add a list at the end as list elementss
# print(l1)


'''insert'''
#takes two values [<index at which element is to insert>,<element>]

# l1=[1,5,6,8]
# l1.insert(2,'yo')
# print(l1)


'''pop'''
# used to remove the element from a list list.pop(<index>)
# l1=[1,5,6,8]
# print(l1.pop(2))         #it will return the removed element from the list
# print(l1)            

# print(l1.pop())          # if no index is written it will remove last element from the index and return it
# print(l1)

'''remove'''
#used to remove the first occurence of the element and does not return nothing list.remove(<element>)

# l1=[1,5,6,5,8]
# l1.remove(5)
# print(l1)

'''sort'''
# l1=[1,5,6,10,55,8]
# l1.sort(reverse=True)   #it will give in descending  order by default it is in increasing order
# print(l1)
