"""num=0
for n in range(10):
    n=n+1
    if(n==5):
        break
    print("number is",n)
print("out of loop")
print("---------------------")
list =[1,2,3,4]
count = 1
for i in list:
    if i == 3:
        print("item matched")
        count = count + 1
        break
print("found at",count,"location")
print("--------------------")
str="srinadh"
for i in str:
    if i=='h':
        break
    print(i)
print("-----------------------")

n=2
while n:
    i=1
    while i<=10:
        print("%d X %d = %d"%(n,i,n*i))
        i=i+1

    print("which table you want")
    n=int(input("enter a number:"))
    if n==0:
        break
print("-------------------")


num=1
for num in range(1,11):
    if num==6:
        print("hi")
        continue
        print("heloo")
        print("he")
    print(num)

    print("list of functions:",dir(str),end=" ,")"""


class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(isinstance(d,Calculation2))




