# aggregation "has a" property
# car has an engine
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
add=Address("Bengaluru","560051","Karnataka")
cust=Customer("nitish","male",add)# here class customer takes adreess details from other class
print(cust.address.pincode) #to access pincode we can acess it from objexct
print(add.state)
