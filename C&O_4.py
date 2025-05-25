class library:
    def __init__(self):
        self.books=[]
    def add_books(self,book):
        self.books.append(book)
        print(self.books)
a=input("Enter the book to be added")
obj=library()
obj.add_books(a)