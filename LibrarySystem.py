class Library:
    def __init__(self):
        self.noOfBook = 0
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        self.noOfBook = len(self.books)
        
        
    def showBook(self):
        print(f"The library has {self.noOfBook} books. The Books are : " )
        for book in self.books:
            print(book)
            
l1 = Library()
l1.addBook("C++")
l1.addBook("Java")
l1.addBook("Python")
l1.showBook()