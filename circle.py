class circle:
    def __init__(self):
        pass
    def area(self,radius):
       return radius*radius
radius=int(input("enter the radius"))
obj=circle()
og=obj.area(radius)
print("The radius of circle is",og)
