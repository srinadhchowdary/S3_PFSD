class student:
    def __init__(self,name):
        print("This is parametereised constructor")
        self.name=name

    def display(self):
        print("hello",self.name)

s=student("srinadh")
s.display()