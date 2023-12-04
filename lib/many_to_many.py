import ipdb

class Author:

    all = []

    def __init__(self, name):
        self.name = name 
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception('name must be of type string')
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        pass
    
class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception('title must be of type string')

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, author):
        if not (isinstance(author, Author) or not author):
            raise Exception("Object is not of type Author")
        self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not (isinstance(book, Book) or not book):
            raise Exception("Object is not of type Book")
        self._book = book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception('date is not of type string')
        self._date = date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception('royalties is not of type int')
        self._royalties = royalties




# author = Author("Name")
# book = Book("Title")
# contract = Contract(author, book, '01/01/2001', 50000)
# print(author.contracts())