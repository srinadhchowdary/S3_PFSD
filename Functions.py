def square(num):
    return num* num

print(square(5))

#BULIT IN FUNCTIONS:
#PRINT():
print("PRINT FUNCTION:")
a=input("enter a number:")
print(a)

#input()
print("INPUT FUNCTION:")
b=input("enter a number:")
print(b)

#absolute():
print("ABSOLUTE FUNCTION FOLLOWS:")
integer = -20
print('Absolute value of -20 is:', abs(integer))
floating = -20.83
print('Absolute value of -20.83 is:', abs(floating))

#bin()
print("BIN FUNCTION FOLLOWS:")
x =int(input("enter a number"))
y =  bin(x)
print (y)

#range()
print("RANGE FUNCTION FOLLOWS:")
x = range(3, 20, 2)
for n in x:
  print(n,end=" ")


#USER-DEFINED:
print(end="\n")
print("USER-DEFINED follows:")
def add(num1,num2):
   return num1+num2

print(add(5,10))




