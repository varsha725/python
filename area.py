#circle.py in Pack_Main
from math import pi
def area_circle(radius):
area = pi * radius * radius
return area
def peri_circle(radius):
peri = 2*pi*radius
return peri
#rectangle.py in Pack_Main
def area_rect(l,b):
area = l*b
return area
def peri_rect(l,b):
peri = 2*(l+b)
return peri
# cuboid.py in Pack_Sub
def volume_cuboid(l,b,h):
vol = l * b * h
return vol
def peri_cuboid(l,b,h):
peri = 4 * (l + b + h)
return peri
"""
Volume of the cuboid = (length × breadth × height)
Perimeter of cuboid = 4 (length + breadth + height)
"""
# sphere.py in Pack_Sub
from math import pi
def surface_area_sphere(radius):
s_area = 4 * pi * radius * radius
return s_area
def volume_sphere(radius):
vol = (4/3) * pi * radius * radius
return vol
"""
Surface Area of a Sphere A = 4 π r2
Volume of a Sphere V = (4 ⁄ 3) π r3
"""

# PackageDemo1
from Pack_Main import circle
from Pack_Main.rectangle import *
import Pack_Main.Pack_Sub.cuboid
from Pack_Main.Pack_Sub import sphere
cArea = circle.area_circle(5)
print("The Area of the Circle is : ",cArea)
cPeri = circle.peri_circle(5)
print("The Perimeter of the Circle is : ",cPeri)
rArea = Pack_Main.rectangle.area_rect(10,5)
print("The Area of the Rectangle is : ",rArea)
rPeri = Pack_Main.rectangle.peri_rect(10,5)
print("The Perimeter of the Rectangle is : ",rPeri)import Pack_Main.Pack_Sub.cuboid as PC
print("Cuboid Volume: ",PC.volume_cuboid(10,5,7))
print("Cuboid Perimeter: ",PC.peri_cuboid(10,5,7))
from Pack_Main.Pack_Sub.sphere import surface_area_sphere
print(surface_area_sphere(5))
print("Cuboid Volume: ",Pack_Main.Pack_Sub.cuboid.volume_cuboid(10,5,7))
print("Cuboid Perimeter: ",Pack_Main.Pack_Sub.cuboid.peri_cuboid(10,5,7))
print("Sphere Surface Area: " , sphere.surface_area_sphere(5))
print("Sphere Volume: " , sphere.volume_sphere(5))
