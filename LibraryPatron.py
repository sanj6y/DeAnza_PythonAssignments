class LibraryPatron():
    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = []
    def checkOutBook(self, checkOutLimit, Book):
        if len(self.booksCheckedOut) < checkOutLimit:
            self.booksCheckedOut.append(Book.title)
            print(self.name, 'has checked out', str(Book.title))
        else:
            print('Sorry', self.name, 'you are at your limit of', str(checkOutLimit), 'books.')
    def returnBook(self, Book):
        title = Book.title
        index = -1
        for i in range(len(self.booksCheckedOut)):
            if self.booksCheckedOut[i] == title:
                index = i
                break
        if index != -1:
            self.booksCheckedOut.remove(title)
            print(self.name, 'has returned', title, '.')
    def printCheckedOutBooks(self):
        print(self.name, 'has the following books checked out:')
        for title in self.booksCheckedOut:
            print(title)
            
class AdultPatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 4
    def checkOutBook(self, Book):
        super().checkOutBook(self.checkOutLimit, Book.title)

class JuvenilePatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 2
    def checkOutBook(self, Book):
        if Book.bookType == 'Juvenile':
            super().checkOutBook(self.checkOutLimit, Book.title)
            print(self.name, 'has checked out', Book.title)
        else:
            print('Sorry', self.name, Book.title, 'is an adult book.')
