#FOR LOOP
numbers=[3,5]
sum= 0
for num in numbers:
    sum = sum + num ** 2
print("The sum of squares is: ", sum)

print("enter a number:")
num=2
for i in range(1,6):
    print(num * i)


#WHILE LOOP:
print("WHILE LOOP FOLLOWS:")
i=int(input("enter a number:"))
while(i>0):
    print(i)
    i-=1

#BREAK
print("BREAK FOLLOWS:")
i = 0
while 1:
    print(i)
    i=i+1
    if i == 10:
        break
print("came out of while loop")

#CONTINUE:
print("CONTINUE FOLLOWS:")
a=0
while a<=5:
    a=a+1
    if a%2!=0:
        continue
    print(a)
print("end of loop")

#PASS:
print("PASS FOLLOWS:")
sequence = {"Python", "Pass", "Statement", "Placeholder"}
for value in sequence:
    if value == "Pass":
        pass
    else:
        print("Not reached pass keyword: ", value)

number=0
for number in range(10):
    number=number+1
    if number==5:
        pass
    print("Number is"+str(number))
print("out of loop")