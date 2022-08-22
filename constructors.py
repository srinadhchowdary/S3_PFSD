class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name


    def display(self):
        print("ID:%d\nNAME:%s"% (self.id,self.name))

s1=student(1,"sri")
s2=student(2,"nadh")

s1.display()
s2.display()