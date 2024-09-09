'''Write a program ro get roll no. names and marks of the students of a class from the user and stor these details in a file clled "marks.txt'''

# a=int(input("enter total number of students : "))
# f=open("practise/mark.txt","w")
# for i in range(0,a):
#     print(f"enter details of student {i+1}")
#     r=int(input("enter roll no. : "))
#     m=int(input("enter marks : "))
#     n=input("enter name : ")
#     str=f'{r},{n},{m}\n'
#     f.write(str)

# f.close()

'''write a program to read a text file line by line and display each word separated by a '#'  '''

# f=open("classes//new.txt","r")
# str=f.read()
# for i in str:
#     if(i==' '):
#         a='#'
#         print(a,end='')
#     else:
#         print(i,end='')
# f.close()


'''write a program to read a text file and display the count of vowels ans consonants in the file '''

# f=open("classes//new.txt","r")
# str=f.read()
# count_v=0
# count_c=0
# for i in str:
#     if(i.lower() in 'aeiou'):
#         count_v+=1
#     elif(i.isalpha()):
#         count_c+=1
# print(f"total number of vowels are {count_v}\ntotal number of consonents are {count_c}")

# f.close()

''' Write a program to read the text from a given file 'poems.txt' and find out 
whether it contains the word 'twinkle'.
'''
# word=input("enter a word: ")
# f=open("classes//new.txt","r")
# str=f.read()
# found=False
# for i in str.split():
#     if(i==word):
#         found=True
# if(found):
#     print(f"yes {word} is present")  
# else:
#     print(f"No {word} is not present") 
# f.close()

'''

 The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file 'hi-score.txt' which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score

'''



# def game():
#     n=int(input("enter : "))
#     return n 

# new_score=game()

# with open("practise/Hi-score.txt","r+") as f:
#     old_score=f.read().strip() # read from the file

#     if old_score:
#         old_score=int(old_score)
#     else:
#         old_score=0
#     if(new_score>old_score):
#         f.seek(0)  # put file pointer at starting position
#         f.write(str(new_score))

'''Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old'''


# def generateTable(i):
#     with open('practise/mark.txt','a') as f:
#         f.write(f'\nTable of {i}\n\n')
#         for t in range(1,11):
#             table=f'{i} x {t} = {i*t}'
#             f.write(f'{table}\n')


# for i in range(1,21):
#     generateTable(i)



''' A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.'''

