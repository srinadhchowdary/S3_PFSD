#SINGLE INHERITANCE
print("single inheritance")
class Parent:
    def func1(self,a,b):
        c=a+b
        print("This function is in parent class.",c)

class Child(Parent):
    def func2(self,c,d):

        e=c+d
        print("This function is in child class.",e)


object = Child()
object.func1(20,30)
object.func2(30,45)


#MULTIPLE INHERITANCE
print("\nMULTIPLE INHERITANCE follows")
class calculation:
    def summation(self,a):
        print(a+100)
class calculation1:
    def mutliplication(self,a):
        print(a*100)
class calculation3(calculation,calculation1):
    def calculation(self,a,b):
        print(a*b*10)

s=calculation3()
s.calculation(20,5)
s.mutliplication(8)
s.summation(11)

#MULTI-LEVEL INHERITANCE:
print("\nMULTI-LEVEL INHERITANCE follows;")
class addition:
    def addition(self,a,b):
        print(a+b)
class multiplication(addition):
    def multiplication(self,a,b):
        print(a*b)
class division(multiplication):
    def division(self,a,b):
        print(a // b)

s=division()
s1=multiplication()
s.division(20,10)
s.multiplication(20,30)
s1.addition(15,15)

#HIERACHIAL INHERITANCE:
print("\nHIERACHIAL INHERITANCE FOLLOWS:")


class Parent1:
    def func_1(self):
        print("This function is defined inside the parent class.")


class Child_1(Parent1):
    def func_2(self):
        print("This function is defined inside the child 1.")


class Child_2(Parent1):
    def func_3(self):
        print("This function is defined inside the child 2.")

o1 = Child_1()
o2 = Child_2()
o1.func_1()
o1.func_2()
o2.func_1()
o2.func_3()

#HYBRID INHERITANCE:
print("\nHYBRID INHERITANCE follows:")
class School:
  def func1(self):
    print("This function is in school.")

class Student1(School):
  def func2(self):
    print("This function is in student 1. ")

class Student2(School):
  def func3(self):
    print("This function is in student 2.")

class Student3(Student1, Student2):
  def func4(self):
    print("This function is in student 3.")

o = Student3()
o.func4()
o.func3()
o.func2()
o.func1()


