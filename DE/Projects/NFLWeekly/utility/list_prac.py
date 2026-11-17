#list
li=[] #define or declare a variable to empty list
print(li,type(li))

li=[1,2,3,'sd',456] #list can have any type of data inside it
print(li)
#accessing list variables
for i in li: 
    print(i,end='\t')
print('\n')
for i in range(len(li)):
    print(i,li[i],end='\t')
print('\n')
#slicing of the list
print(li[:])
print(li[1:])
print(li[-2:])
print(li[::-1])

#list functions
li.append('honey')
print(li)
lis=[]
lis=li.copy() #shallow copy one change doesnt change other
print(li, lis)
li.append('long')#add at the end
print(li,lis)
li_copy=li #deep copy one variable changed effects others
li.insert(1,'dope')
print(li,lis,li_copy)
li_copy.insert(0,'NFL') #insert at a specific index value
print(li,li_copy,lis)
print(li.count(1))#count a specific value
li.extend(lis)
print(li_copy)
li.append(lis)
print(li_copy)
print(li.index('NFL'))#results in the index of the object in the list 
li.pop