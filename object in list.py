class Customer:
    def __init__(self,name):
        self.name=name
c1=Customer("nitish")
c2=Customer("nitish2")
c3=Customer("nitish3")
print(c2.name)
l=[c1,c2,c3]
for i in l:
    print(i.name)
    # heere i is acting as object 
