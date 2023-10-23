eng=input("enter your english marks out of 100 : ")
sci=input("enter your science marks out of 100 : ")
sst=input("enter your sst marks out of 100 : ")
urdu=input("enter your urdu marks out of 100 : ")
mat=input("enter your maths marks out of 100 : ")
com=input("enter your computer marks out of 100 : ")
isl=input("enter your islamiat marks out of 100 : ")
total =float(sci) + float(com) + float(isl) + float(sst) + float(eng) + float(urdu) + float(mat) 
print("your total marks are  : " , total )
per= float(total/700 * 100)
print("your percentage is :" ,per)

if per >=80 :
    print("your Grade is A+")

elif per >=70 :
    print("your Grade is A")

elif per >=60 :
    print("your Grade is B")

elif per >=50 :
    print("your Grade is c")

else :
    print("you are fail ")