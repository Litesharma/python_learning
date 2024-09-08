'''# Data files are of two types 
1.) text files 
2.) Binary files
 
1.) text files also called regular text files-> which stores the text in the same format as typed and uses the files extensions like ".txt"

Regular text file content .txt--> I am simple text.
TSV(tab seprated values) .tsv --> I    am    simple    text.
CSV(comma seprated values) .csv--> I,am,simple,text.

'''

# opening and closing a file

'''
In order to work with file we need to open it first in a specific mode 
to open a file use open() function 
<file-ObjectName> =open(<fileName>,<mode>) 

different types of mode are there 
most comman are :-
read(r)
write(w)
append(a)

// if no mode is written by default file open in read mode
'''
# file_handle=open("classes/new.txt")
# f=file_handle.read()
# print(f)

''' file-object is also known as file-handle
it is very usefull tool in python by this only a python program can work with file stored on hardware '''

# a file object is a reference to a file on disk . it opend and maked it available for a number of different tasks.


'''
--------------------------------------------------
file Access modes:
sr.|text file Mode|Binary file mode | Description| Noted
1  |    'r'       |       'rb'      |  read only | file must exist already otherwise it will return error   
2  |    'w'       |       'wb'      | write only | if the file not exist , file is created 2.)if the file already exists, it will truncate existing data and over-write in the file .So this mode must be used with caution   
3  |    'a'       |       'ab'      |  append    | if the file not exist , file is created 3.)file is in "write" only mode 2.) if the file already exist , the file data is retained and new data being written will be appended to the end.   
4  |    'r+'      |   'r+b'or'rb+'  |read & write| file must exist already otherwise it will return error2.)both reading and writing task can be take place  
5  |    'w+'      |   'w+b'or'wb+'  |write & read| if the file not exist , file is created 2.) if the file exist file is truncated (past data will be lost)3.) both reading and writting task can take place   
6  |    'a+'      |   'a+b'or'ab+'  |write & read| if the file not exist , file is created 2.) if the file exist file's existing data retained new data is appended 3.) both reading and writting task can take place   
'''