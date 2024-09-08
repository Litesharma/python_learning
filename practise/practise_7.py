'''Write a program to print multiplication table of a given number using for loop.'''

# n=int(input("enter a number : "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

'''using while loop'''
# i=1
# while(i<11):
#     print(f"{n} x {i} = {n*i}")
#     i+=1

'''Write a program to greet all the person names stored in a list l and which starts 
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]'''

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     for a in i:
#         if(a=="S"):
#             print(f'Good Morning {i}')
#             break

''' Write a program to find whether a given number is prime or not.'''


# n=int(input("enter a number : "))
# is_prime=True
# if(n<=1):
#     is_prime=False
# for i in range(2,n):
#     if(n%i==0):
#         is_prime=False

# if(is_prime):
#     print(f'{n} is a prime number')
# else:
#     print(f'{n} is not a prime number')

'''Write a program to find the sum of first n natural numbers using while loop.'''

# n=int(input("enter a number : "))

# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     i+=1
# print(f'sum of first {n} natural number is {sum}')
    

'''Write a program to calculate the factorial of a given number using for loop'''
        

# n=int(input("enter a number : "))
# fact=1
# for i in range(n,0,-1):
#     fact*=i
# print(f'factorial of {n} is {fact}')

'''star patteren 
  *
 *** 
*****
'''

# n=int(input("enter a number : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(i*2-1),end="")
#     print('')

'''
*
**
***
'''
# n=int(input("enter a number : "))
# for i in range(1,n+1):
#     print("*"*(i),end="")
#     print("")


'''
* * *
*   * 
* * *
'''
# n=int(input("enter a number : "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#         print("")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#         print("")


'''Write a program to print multiplication table of n using for loops in reversed 
order'''

# n=int(input("enter a number : "))
# a=10
# for i in range(1,a+1):
#     print(f'{n} x {a} = {(a)*n}')
#     a-=1
