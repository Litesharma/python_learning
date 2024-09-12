'''
polymorphism :> when the same operator is allowed to have different meaning according to the context
1+2=3
"raj"+"u"="raju"
see here context is changing and meaning of "+" is changing 
and to define our meaning of +,- etc. of our class with the help of dunder function  

'''
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def showCompNum(self):
#         if self.img >= 0:
#             print(f'{self.real}+{self.img}i')
#         else:
#             print(f'{self.real}{self.img}i')

#     def __add__(self, num2):                            # __add__ dunder function 
#         new_real = self.real + num2.real
#         new_img = self.img + num2.img
#         return Complex(new_real, new_img)

# # Create instances of Complex
# num1 = Complex(4, 5)
# num2 = Complex(3, -2)
# num1.showCompNum()
# num2.showCompNum()
# num3=num1+num2
# num3.showCompNum()
# result = num1.add(num2)                   # i just want to do that num1+num2 but here i have to call a lots of function to avoid this i will use deunder function
# result.showCompNum()  

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
    
#     def showCompNum(self):
#         a="+"
#         if(self.img<0):
#             a=""
#         print(f'{self.real}{a}{self.img}i')


#     def add(self,num2):
#         newReal=self.real + num2.real
#         newImg=self.img + num2.img
#         a="+"
#         if(newImg<0):
#             a=""
#         return f'{newReal}{a}{newImg}i'

# num1=Complex(4,5)
# num1.showCompNum()
# num2=Complex(3,2)
# sum=num1.add(num2)
# print(sum)
