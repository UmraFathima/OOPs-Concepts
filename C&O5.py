class Customer:
    def __init__(self,name):
        self.name=name
        # self.gender=gender
# here customer is acting as new cust inside the function
# something chnaged inside th function is chnged throughout

def greet(customer):
    print("Hello",customer.name)
cust=Customer("Nititsh")
greet(cust)