from math import *
class Calculate:
        def rectangle(self,l,b):
            print("Area of Rectangle:",l * b)
            print("Perimeter of Rectangle:",2*(l+b))
        def triangle(self,s1,s2,s3,h):
            print("Area of triangle:",(0.5*s3*h))
            print("Periemter of triangle",s1+s2+s3)
        def circle(self,r):
            print("Area of circle",pi*r*r)
            print("Periemter of circle",2*pi*r)




r=Calculate()
r.rectangle(10,20)
r.triangle(10,23,12,43)
r.circle(5)