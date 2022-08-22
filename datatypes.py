#NUMERIC
a=5
print(a)
print(type(a)) #int
b=9.4
print(b)
print(type(b))  #float
c=5+6j
print(c)
print(type(c)) #complex
print("c is complex number",isinstance(c,complex))

#BOOLEAN
print("BOOLEAN FOLLOWS:")
print(type(True))
print(type(False))

#DICTIONARY
print("DICTIONARY FOLLOWS:")
dic={1:"srinadh",2:"Bejawada",3:"chowdary",4:"Ramarao",5:"Rambabu",6:"Madhavi",7:"Lakshmi Thanuja"}
print(type(dic))
print(dic[1])
print(dic.keys())
print(dic.values())
dic.clear()
print(dic.values())

#SET
print("SET FOLLOWS:")
set1=set()
set2={5,"srinadh",9.5,"Bejawada",23.566,}
print(set1)
print(set2)
set2.add(999)
print(set2)
set2.remove(9.5)
print(set2)

#SEQUENCE
   #1.STRINGS
print("STRINGS FOLLOWS:")
s="PFSD"
print(s)
print(type(s))
s1="HELLO "
s2=" welcome to PFSD course"
print(s1[3])
print(s2[9])
print(s1*3)
print(s1+s2)
print(s1[0:3])
print(s2[12:25])
print(s2.capitalize())#capitalize 1st letter
print("no of O's in S2",s2.count('o'))
print(s2.upper())
print(s1.lower())

 #2.LIST
print("LIST FOLLOWS:")
list1=[5,'HELLO','PYTHON! ','THIS ','IS','SRINADH',2.0,'VERSION!']
print(list1[2])
print(list1[0:2])   #range
print(list1[2:])  #slicing
print(list1*4)   #repeatition
print(list1+list1)  #concatnation
print(list1[-1: :-1]) #reverse
print(list1[-4:-1])
del list1[3]     #delete
list1[3]='RRR'  #add
print(list1)
list1.append(1000) #addiing last
print(list1)
print(len(list1))   #length
list1.insert(3,'ram') #insert
print(list1)

   #3.TUPLE
print("TUPLE FOLLOWS:")
tuple1=(5,"hello","PFSD",9.2,18)
print(tuple1[2])
print(tuple1[1:4])
print(tuple1[2:])
print(tuple1*3)
print(tuple1+tuple1)
print(tuple1)
print(len(tuple1))