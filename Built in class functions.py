class student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

s=student(101,"srinadh",18)
print(getattr(s,'name'),getattr(s,'id'),getattr(s,'age'))
setattr(s,'age',22)
setattr(s,'name',"RAMARAO")
print(getattr(s,'name'),getattr(s,'age'))
print(hasattr(s,'id'),hasattr(s,'room'))
delattr(s,'age')
print(s.age)
