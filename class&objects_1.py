
class A:
    def __init__(self):
        self.name = "Arav"
        self.age = 18
        self.id = 1
        self.display()

    def display(self):
        print(self.name)
        print(self.age)
        print(self.id)

obj_a = A()



class B:
    def __init__(self):
        self.name = "Arav"
        self.age = 18
        self.id = 1

    def display(self):
        print(self.name)
        print(self.age)
        print(self.id)

obj_b = B()
obj_b.display()
