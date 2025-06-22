class Customer:
    def __init__(self,name):
        self.name=name
def greet(customer):
    print("HELLO",customer.name) #here the customer name is nitish as passed by refernce
    customer.name="Aakash"
    print(customer.name) # here we are changing the name of the customer as it chnaged in the function it is changed thru out
obj=Customer("Ankita")
greet(obj)