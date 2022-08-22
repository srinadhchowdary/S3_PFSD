#if:
print("IF FOLLOWS:")
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>b and a>c:
    print("a is largest")
if b>a and b>c:
    print("b is largest")
if c>a and c>b:
    print("c is greatest")

#if else
print("IF ELSE FOLLOWS:")
a=int(input("enter a number:"))
if a<10:
	print("helloo")
else:
	print("Greater")

#NESTED IF:
print("NESTED IF FOLLOWS:")
a =int(input("enter a number:"))
if a < 10:
    if a < 7:
        print(a)
else:
    print("wrong")

#ELIF:
print("ELIF FOLLLOWS:")
a =int(input("enter a number:"))
if a < 3:
    print(a)
elif a < 2:
    print(a)
elif a == 6:
    print(a)
elif a == 7:
    print(a)
else:
    print("condition fails")
