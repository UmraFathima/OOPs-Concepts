class Atm:
    def __init__(self):
        self.balance=0
    def displayBalance(self):
        print(self.balance)
    def deposit(self):
        a=int(input("Enter the amount to be deposited"))
        self.balance+=a
        print("The deposited Amount",self.balance)
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
