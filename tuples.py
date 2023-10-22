#creating tupple
tuple3=("bat" , "ball" , "racket")
print(tuple3)

#type 
print(type(tuple3))

#one item tupple / use coma for single item otherwise it will be become str
tuple1=("appple,")
print(type(tuple1))

#accessing tuple3
print(tuple3[1])
print(tuple3[-1])
print(tuple3[0:2])
print(tuple3[-2:-1])

#checking items in tuple3
if "bat" in tuple3 :
    print("yes")
else :
    print("no")

if "bat" in tuple3 :
    print("yes")
else :
    print("no")

  
if "bat" and "ball" in tuple3 :
    print("yes")
else :
    print("no")  

#changing tuple3 into list for changing items
x=list(tuple3)
print(x)
x[1]="football"
print(x)
print(type(x))
tuple3=tuple(x)
print(tuple3)
print(type(tuple3))


#adding tuple3 to tuple3
y=("egg")
y += tuple3
print(tuple3)

#deleting tuple
del tuple3
print(tuple3)

