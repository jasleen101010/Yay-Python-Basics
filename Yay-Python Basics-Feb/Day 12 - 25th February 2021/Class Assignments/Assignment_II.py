"""
    WAP using OOPs where you need to design a Library Management System.
    attributes : book_name, book_no, author_name, author_no, librarian_name, name_of_the_library [Book, Author]
"""

# Program [Answer]


# `Book` Class
class Book:

    no_of_books = 0                                # Class Variable

    # Class Constructor
    def __init__(self, name, number):
        self.book_name = name                      # Instance Variables
        self.book_no = number
        Book.no_of_books += 1                      # Updating Class Variable

    # Method `showBook()` to display off the Books Available
    def showBook(self):
        print(f"Book Serial Number : {self.book_no} and it's Name : {self.book_name}")


# `Author` Class
class Author:

    no_of_authors = 0                               # Class Variable

    # Class Constructor
    def __init__(self, name, number):
        self.author_name = name                     # Instance Variables
        self.author_no = number
        self.book_names = []
        Author.no_of_authors += 1                   # Updating Class Variable

    # Method `showAuthor()` to display off the Authors Available
    def showAuthor(self):
        print(f"Author Serial Number : {self.author_no} and Name : {self.author_name}")
        print(f'And the Book(s) associated with this Author : {[i.book_name for i in self.book_names]}')

    # Method `addBook()` to add Books associated with a particular Author
    def addBooks(self, bookDetails):
        if isinstance(bookDetails, list):
            self.book_names.extend(bookDetails)
        else:
            self.book_names.append(bookDetails)


# `Library` Class
class Library:

    name_of_library = 'YAY-Python Library'           # Class Variables
    no_of_books = 0
    no_of_authors = 0

    # Class Constructor
    def __init__(self):
        self.books = []                              # Instance Variables
        self.authors = []
        Library.no_of_books = Book.no_of_books       # Updating Class Variables
        Library.no_of_authors = Author.no_of_authors

    # Method `addBooks()` to add Books present in the Library
    def addBooks(self, list_of_books):
        self.books.extend(list_of_books)

    # Method `addAuthors()` to add Authors present in the Library
    def addAuthors(self, list_of_authors):
        self.authors.extend(list_of_authors)

    # Method `checkBook()` to add check whether a Book is present in the Library
    def checkBook(self, bookName):
        flag = 0
        for bookInfo in self.books:
            if bookName == bookInfo.book_name:
                print(f'Yes, the Book "{bookName}" exists in our Library!')
                return
        if not flag:
            print("Sorry, the Book you asked for isn't available at the Moment!")

    # Method `checkAuthor()` to add check whether a Author is present in the Library
    def checkAuthor(self, authorName):
        flag = 0
        for authorInfo in self.authors:
            if authorName == authorInfo.author_name:
                print(f'Yes, Author "{authorName}" exists in our Library!')
                return
        if not flag:
            print("Sorry, the Author you asked for isn't available at the Moment!")


# Main Method
def main():

    # Defining the Books
    book1 = Book('Mein Kampf', 707000)
    book2 = Book('The Godfather', 86845)
    book3 = Book('The Sicilian', 4589535)
    book4 = Book('Hamlet', 655465)

    # Defining the Authors
    author1 = Author('Adolf Hitler', 1)
    author2 = Author('Mario Puzo', 7)
    author3 = Author('William Shakespeare', 2)
    author4 = Author('Chetan Bhagat', 60)
    author5 = Author('Any Random Name', 999)

    # Associating the Books with the Authors
    author1.addBooks(book1)
    author2.addBooks([book2, book3])
    author3.addBooks(book4)

    # Defining the Books and Authors Present in the Library
    library = Library()
    library.addBooks([book1, book2, book3, book4])
    library.addAuthors([author1, author2, author3, author4, author5])

    # Displaying out Information
    print(f'Name of the Library : {library.name_of_library}')
    print(f'No. of Books in the Library : {library.no_of_books}')
    print(f'No. of Authors in the Library : {library.no_of_authors}')
    book1.showBook()
    author2.showAuthor()
    author1.showAuthor()
    author4.showAuthor()
    library.checkBook('The Jungle Book')
    library.checkBook('Hamlet')
    library.checkAuthor('Adolf Hitler')
    library.checkAuthor('Rahul Bordoloi')


# Driver Function
if __name__ == '__main__':
    main()