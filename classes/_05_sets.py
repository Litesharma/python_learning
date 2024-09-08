#sets

s=set()  #to create an empty set use this do not use {} too create an empty set this is use for dictonary

s={1,2,3,5,7,66,6,6,6,6}  # set me elements repeat nahi ho sakte 
t={5,6,8,88,1,3}
p={1,2,9,6,5}
print(t.union(p))   # answer is in increasing order
print(p.union(t))   #same answer
print(p.intersection(t))  # again answer is in increasing order