#7. Write a program to create a list and perform various operations on list using menu
'''
list=[10,20,80,50]
print("List=",list)

print("---Append Method---")
list.append(50) #One element will add at a time
print("List=",list)


print("---Count Method---")
print("list of count=",list.count(50))

print("----Extend Method---")  #It will merge two list
lst1=['Abhishek','raj','savan']
lst2=[10,50,80,100]
lst1.extend(lst2)
print(lst1)
print(lst2)


print("-----Index Method------")
print("Index of Abhishek=",lst1.index('Abhishek'))

print("----Insert Method-----")
lst1.insert(1,'Vraj') #We need to speicfie the index in which index i need to insert
print(lst1)
'''
lst1=['Abhishek','raj','savan']
print("----Pop Method----")
lst1.pop()  #It will remove last element from list
print(lst1)

print("----Remove Method-----") # It will remove specific element which we wanted to remove
lst1.remove('raj')
print(lst1)























