# A wire is the form of Arc at an angle of 60 degrees and
# the radius of the arc is 42. The wire is converted into a square. Find the area of the square.
angle = int(input("Enter angle: ")) #input angle
radius = int(input("Radius: "))
pi = 3.14
lengthOfWire = (angle / 360)*2*pi*radius
side = lengthOfWire/4
area =side**2
print("area of square is: ",area)
