class library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    
    def addBook(self , book):
        self.books.append(book)
        self.noBooks = len(self.books)
        
        def showInfo(self):
            print(f"The library has {self.noBooks} books. ")
l1 = library()
l1.addBook("Harry Porter")
l1.addBook("The Lord of the Rings")
l1.addBook("The Hobbit")
l1.showInfo()
# bhdk error kru hai ye
