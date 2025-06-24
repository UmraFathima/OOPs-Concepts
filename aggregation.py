# aggregation "has a" property
# car has an engine
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,new_name,new_city,new_pin,new_state): #this line and nxt to nxt line is imp to remeber
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state) #here we are calling new method from another class
class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    def change_address(self,new_city,new_pincode,new_state):
        self.city=new_city
        # self.new_pincode=new_pincode we shpuld not creeate new var keep it samejus change val "WRONG"
        self.pincode=new_pincode
        self.state=new_state
add=Address("Bengaluru","560051","Karnataka")
cust=Customer("nitish","male",add)# here class customer takes adreess details from other class
print(cust.address.pincode) #to access pincode we can acess it from objexct
# print(add.state)
# add.change_add("kolkatta",700012,"WB")
# cust.edit_profile("Aakash",add)


# edit profile
cust.edit_profile("jhon","agra","450008","Delhi")