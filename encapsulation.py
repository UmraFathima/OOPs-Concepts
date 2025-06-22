class Atm():
    def __init__(self):
        self.__balance=0
        self.__pin="12"
    def get_Pin(self):
        return self.__pin
    def set_Pin(self,newpin):
        if  type(newpin)==str:
            self.__pin=newpin
            print(self.__pin)
# print(self.__pin)
# nothing in python is truly private
sbi=Atm()
sbi.get_Pin()
sbi.set_Pin("1234")