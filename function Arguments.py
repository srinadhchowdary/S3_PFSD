#FUNCTION ARGUMENTS:
#1.DEFAULT ARGUMENTS:
def sample(num1,num2=10):
	 print("num1 is",num1)
	 print("num2 is",num2)

sample(5)

#2.KEYWORD ARGUMENTS:
print("KEYWORD ARGUMENTS:")
def sample(num1,num2):
    print("num1 is", num1)
    print("num2 is", num2)

sample(num2=10,num1=20)

#3.REQUIRED ARGUMENTS:
print("REQUIRED ARGUMENTS FOLLOWS:")
def sample(num1, num2):
    print("num1 is", num1)
    print("num2 is", num2)

sample(10,5)
