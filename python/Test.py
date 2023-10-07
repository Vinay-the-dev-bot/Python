#Creating a string
pancard_number="AABGT6715H"
#Length of the string
print("Length of the PAN card number:", len(pancard_number))
#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)
print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print("something" ," ", index ," ", pancard_number[index])
    
print("Iterating the string using keyword in")
for value in pancard_number:
    print("something2" ," ", value ," ", value)
print("Searching for a character in string")
if "T" in pancard_number:
    print("Character is present")
else:
    print("Character is not present")
#Slicing a string
print("The numbers in the PAN card number:", pancard_number[5:9])
print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])
print(pancard_number)
print(pancard_number[0:6])
if "name1" in name:
    print ("Name1 is present in name")
else:
    print("Name1 is not present in name")
print("111"*123)
print(111*123)
print("KJDVS")
x = "Python"
y = "is"
z = "awesome"
print("X + Y + Z :" , x + y+ z)
print("x,y,z :" + x,y,z)
mylist = ["apple", "banana", "cherry"]
print( mylist)
num1 = 0
num2 = 23
if num1>num2:
    print("Num1 is greater")
else:
    print("Num2 is greater")
print("1%4 =" , 1%4)
for i in range(num1,num2):
    print("I",i,"Hello")
print("sihbfv",  (153 % 7) + (213 % 4))
print( 5+10*2)