#list
list=["apple","mango","banana","cherry","lemon"]
print(list)

#length of list
print(len(list))
#access list items
print(list[2])
print(list[-2])

#range of idexes
print(list[1:4])
print(list[:4])
print(list[3:])
print(list[-4:-1])

#checking items in list
if "mango"  in list :
 print("yes,available")
else :
 print("not available")

if "mango" and "bnana" in list :
 print("yes,available")
else :
 print("not available")

if "mango" or "bnana" in list :
 print("yes,available")
else :
 print("not available")


#type 
print(type(list))

 #change item in list
list[1]="leeche"
print(list)

#insert in list
list.insert(2,"hello")
print(list)

#append in list
list.append("aro")
print(list)

#extend in list
newlist="ali","hamza"
list.extend(newlist)
print(list)

#remove in list
list.remove("hello")
print(list)

#pop in list
list.pop(4)
print(list)

#pop is LIFO
list.pop()
list.pop()
print(list)

#delete items in list
del list[-2]
print(list)

#delete list completely
#del list
print(list)

#clear list items only
#list.clear()
print(list)

#for loop in list
for x in list :
 print(x)
 
#while loop in list
i=0
while i < len(list) :
 print(list[i])
 i=i+1
 
 #adding item in new list from existing list
fruits=[]
for x in list :
  if "a" in x :
   fruits.append(x)
   print(list)
   print(fruits)  

  #upper case in list
  list2=[x.upper() for x in list] 
  print(list2)

  #sorting in list in ascending order
  list.sort()
  print(list)

  #sorting in list in descending order
  list.sort(reverse=True)
  print(list)

  #sorting numbers in list
  num=[100,59,85,99,42,62]
  num.sort()
  print(num)

#sorting with buit in keyfunction
list.sort(key=str.lower)
print(list)
list.reverse()
print(list)

#joining two list
list1=[1,2,3,4,5]
list3=[6,7,8,9,10]
numlist=list1 + list3
print(numlist)

#joining list with loop
list1=[1,2,3,4,5]
list3=[6,7,8,9,10]
for x in list3 :
 list1.append(x)
 print(list1)

list.count("apple")
print(list)
 
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list