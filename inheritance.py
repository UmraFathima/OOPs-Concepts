# few examples of inheritance
# child cannot inherit private variable of parent class
# we can inherit contructor as well

# ****************example of simple inheritance***********************
class parent:
    def login(self):
        print("login")
    def reg(self):
        print("Reg")
class Child(parent): #here we say class child inherits the parent clsaa
    def enroll(self):
        print("enroll")
ab=Child()
ab.login()
ab.enroll()

# ***********inheriting the constructor******************
class parent:
    def __init__(self,name):
        self.name=name 
    def login(self):
        print("login")
    def reg(self):
        print("Reg")
class Child(parent): #here we say class child inherits the parent clsaa
    def enroll(self):
        print("enroll")
abc2=Child("chang") # here we are passing a value of contrctor to the object of child class but child does not have constructor
# but child inherit parent class and patrent have contructor so the value of name will be in parents class constructor
print(abc2.name)

########################inheriting private variables#####################################################################

class parent:
    def __init__(self,name):
        self.__name=name #if we make private var in parent class the child cannot inherit it
    def login(self):
        print("login")
    def reg(self):
        print("Reg")
class Child(parent): #here we say class child inherits the parent clsaa
    def enroll(self):
        print("enroll")
abc=Child("chang")
print(abc.__name) #here it gives error as we cannot inherit it frm parent class

####################################polymorphism --> method overriding --->"class the method of its own class"#########################################################

class parent:
    def login(self):
        print("login")
    def reg(self):
        print("Reg")
    def same(self):
        print("This is Parent class ")
class Child(parent): #here we say class child inherits the parent clsaa
    def enroll(self):
        print("enroll")
    def same(self):
        print("This is Child class ")


abc1=Child()
abc1.same() # as parent and child class has same methids it calss its own class mthod i.e child not the parent so o/p will be this is child class


# I************showing whn constructor is triggered********

class parent:
    def __init__(self,num):
        self.__num=num # here evn though its private we can get it by get method as get method is not private
    def get_num(self):
        return self.__num 
class Child(parent):
    def show(self):
        print("This is teh child class")
son=Child(100)
print(son.get_num()) # here we can get the provate var of parent class
son.show()
# also this example shows that the as oly wen the parent class constructor is triggered thn oly we can derive the instance var from it
# remeber it for nxt example


# exapmle 2
class Parent:
    def __init__(self,num):
        self.__num=num # here evn though its private we can get it by get method as get method is not private
    def get_num(self):
        return self.__num 
class Child(parent):
    def __init__(self,val,num) # here there is a const in the child class as well so now the values will be storedin child class get
        self.__val=val
    def get_val(self):
        return self.__val
son1=Child(100,10)
print(son1.get_num()) # here we can get the private var of parent class
# here the main thig to say is wn we have child cons parent cons wont be triggered 



# *****************Super key********************

class Parent:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def buy(self):
        print("Parent")
class Child(Parent):
    def buy(self):
        print("Child")
        super().buy()   #it is used to called buy class from parent class
cd=Child("Suzuki",67770)
cd.buy()  # as this calls buy of child class
# super key word wont work outside a classs & o/p will be both


###********************************YYYYYYYYYY**************#####
class A:
    def __init__(self,var1):
        self.var1=100
    def display(self,var1): #as this display func is printing self.var1 val...but 200 is stored in self.var1

        print("A"self.var1)
class B(A):
    def display2(self,var1):
        print("B",self.var1)
obj=B(200)
obj.display(200) #evn tho we are passing 200 but the o/p will be 100 as this display func is printing self.var1 val...but 200 is stored in self.var1


class A:
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
class B(A):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera) #we can call const of parent class using super. 
        #here the os and ram val is saved in child class. rest the vals are passed on to the parent class constt
        self.os=os
        self.ram=ram
cs=B(2000,"samsung","32mgp","Android","23g")
print(cs.os)
print(cs.ram)



class A:
    def __init__(self,num):
        self.num=num
    def get_num(self):
        return self.num
class B(A):
    def __init__(self,num,val):
        super().__init__(num)
        self.val=val
    def get_val(self):
        return self.val
de=B(100,200)
print(de.get_num())
print(de.get_val())



class A:
    def __init__(self):
        self.num=100
class B(A):
    def __init__(self):
        super().__init__() #here the parent constr is triggered so the .num val is init to 100 oly then
        self.var=200
    def show(self):
        print(self.num) #here we r able to fetch tht val
        print(self.var)
re=B()
re.show()


class A:
    def __init__(self):
        self.num=100
    def show(self):
        print(self.num)
class B:
    def __init__(self):
        super().__init__()
        self.var=200
    def show(self):
        print(self.var)
yo=A()
yo.show()
yoo=B()
yoo.show()
        
 ########################************multilevel inheritance*************############

class Product:
    def review(self):
        print("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(20000, "Apple", 12)
p = Phone(1000, "Samsung", 1)

s.buy()
s.review()
p.review()



##########***********************multiple inheritance***********##########
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Product:
    def review(self):
        print("Customer review")

class SmartPhone(Phone, Product):
    pass

s = SmartPhone(20000, "Apple", 12)
s.buy()
s.review()



#######**********MRO method resolution order****#####################################
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Product:
    def buy(self):
        print("Product buy method")

class SmartPhone(Phone, Product): # as we r inheriting phone first so 
    pass

s = SmartPhone(20000, "Apple", 12)
s.buy() # the phone class buy will be cllaed 

# MRO
 #####*****************
class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40

class C(B):
    def m2(self):
        return 20

obj1 = A()
obj2 = B()
obj3 = C()

print(obj1.m1() + obj3.m1() + obj3.m2())
#here it follows priority which is claed fist
#obj1.m1 will call class A m1 method
# obj3.m1 will call b class m1 mthod coz class c is inheriting first B class so its mth is given priority
# obj3.m2 will call C class m2 mthod coz class c has its own mthd so it doesnt go further so its mth is given priority
