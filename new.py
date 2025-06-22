# instance variable -->balance and pin in atm which is diff for alll the customer

# static variable are those variable which have the same value for all the customer like serial nummber
# like ifsc code or bank name...... when the customer get added to bank
# static var are outside the contructor inside the class
# instance var are inside the cunstorctor

class Atm:
    __counter=0 #static var to acces it we use class name not objc name
    def __init__(self):
        self.balance=0
        self.sno=Atm.__counter
        Atm.__counter=Atm.__counter +1
    def displayBalance(self):
        print(self.balance)
    def deposit(self):
        a=int(input("Enter the amount to be deposited"))
        self.balance+=a
        print("The deposited Amount",self.balance)

    @staticmethod      #to access this we dont require object we can acces by its class name like Atm.get_counter
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__counter=new
        else:
            print("Not Allowed")

    def withdraw(self):
        b=int(input("Enter the amount to be withdrawn"))
        if b < self.balance:
            self.balance-=b
        else:
            print("Insufficient balance")
obj=Atm()
print("Enter 1 to display balance, 2 to deposit,3 to withdraw")
c=int(input())
if c==1:
    obj.displayBalance()
elif c==2:
    obj.deposit()
elif c==3:
    obj.withdraw()
else:
    print("Check the input")
print(Atm.get_counter())
print(Atm.set_counter(3))
print(Atm.get_counter())