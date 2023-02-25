'''
Sanjay Chandrasekar
Exercise J
CIS 41A Spring 2021
'''

import LibraryBook
import LibraryPatron

def main():
    book1 = LibraryBook.Book("Alice in Wonderland", "Juvenile")
    book2 = LibraryBook.Book("The Cat in the Hat", "Juvenile")
    book3 = LibraryBook.Book("Harry Potter and the Sorcerer's Stone", "Juvenile")
    book4 = LibraryBook.Book("The Hobbit", "Juvenile")
    book5 = LibraryBook.Book("The Da Vinci Code", "Adult")
    book6 = LibraryBook.Book("The Girl with the Dragon Tattoo", "Adult")

    patron1 = LibraryPatron.JuvenilePatron("Jimmy")
    patron2 = LibraryPatron.AdultPatron("Sophia")

    patron1.checkOutBook(book6)
    patron1.checkOutBook(book1)
    patron1.checkOutBook(book2)
    patron1.printCheckedOutBooks()
    patron1.checkOutBook(book3)
    patron1.returnBook(book1)
    patron1.checkOutBook(book3)
    patron1.printCheckedOutBooks()
    patron2.checkOutBook(book5)
    patron2.checkOutBook(book4)
    patron2.printCheckedOutBooks()
    
main()

'''
Execution Results:
Sorry Jimmy The Girl with the Dragon Tattoo is an adult book.
Jimmy has checked out <built-in method title of str object at 0x7fd4e0a8f7b0>
Jimmy has checked out Alice in Wonderland
Jimmy has checked out <built-in method title of str object at 0x7fd4e0a8f760>
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
<built-in method title of str object at 0x7fd4e0a8f7b0>
<built-in method title of str object at 0x7fd4e0a8f760>
Sorry Jimmy you are at your limit of 2 books.
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Sorry Jimmy you are at your limit of 2 books.
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
<built-in method title of str object at 0x7fd4e0a8f7b0>
<built-in method title of str object at 0x7fd4e0a8f760>
Sophia has checked out <built-in method title of str object at 0x7fd4e0a8f710>
Sophia has checked out <built-in method title of str object at 0x7fd4e05998f0>
Sophia has the following books checked out:
<built-in method title of str object at 0x7fd4e0a8f710>
<built-in method title of str object at 0x7fd4e05998f0>
'''