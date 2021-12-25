# This script has the Books functions that will be used in the main.py
import math
import datetime
import json
import pickle
import copy

class Books:
    """
    A class that represents the books in library
    """
    
    def __init__(self,book_id,book_name,book_author,book_published_year,book_type,book_copies):
        """
        A constructor of a book object
        :param book_id: The unique number of the book itself
        :param book_name: The name of the book
        :param book_author: The author of the book
        :param book_published_year: The date the book was published
        :param book_type: The type of book between the options (1= up to 10 days to loan, 2= up to 5 days to loan, 3= up to 2 days to loan)
        :param book_copies: The number of copies in the library
        """
        
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_published_year = book_published_year
        self.book_type = book_type
        self.book_copies = book_copies
    
# books_library = [{"book's ID": [],  #:book_id,
#                   "book's Name": [],  #:book_name,
#                   "book's Authors": [],  #:book_author,
#                   "book's Published year": [],  #:book_published_year,
#                   "book's Type": [],  #:book_type,
#                   "book's Copies": []}]
books_library = {"Books": []}

def add_new_book(book_id,book_name,book_author,book_published_year,book_type,book_copies):
    new_book = books_library["Books"].append({"Book's ID":{book_id},"Book's Name":{book_name},"Book's Authors":{book_author},"Book's Published year":{book_published_year},"Book's Type":{book_type},"Book's Copies":{book_copies}})
    
    with open('books_data.pkl', 'wb') as books_save:
        pickle.dump(books_library, books_save)
        
    return new_book

def display_all_books(books_library):
    """
    :return: all the books in the books, library
    """
    with open('books_data.pkl', 'rb') as books_read:
        books_library = pickle.load(books_read)
    
    return books_library
    
def find_book_by_name(book_name, books_library):
    """
    A search function for searching books in the library by their names
    :param book_name: The name of the book to search
    :param book_library: All the books in library"""
        
    for book in range(len(books_library["Books"])):
        if book_name in books_library["Books"][book]["Book's Name"]:
            return f"{book_name} is in the customers library list"
    else:
        return f"There is no such '{book_name}' book in the library."
    
    
def delete_book(book_name, books_library):
    """
    A function that update the collection of books that in the library, without deleting one.
    :param book_name: The name of the book to delete.
    :param books_library: A collection of all the books in library
    """
    
    for book in range(len(books_library["Books"])):
        if book_name in books_library["Books"][book]["Book's Name"]:
            print(f"Are you sure you want delete '{book_name}' from the library?, y/n: ")
            identifier = input()
            identifiers = ['y','n']
            while identifier not in identifiers:
                print("Please answer with y or n")
                print("Are you sure you want to delete this book?: ")
                identifier = input()
            if identifier == 'y':
                books_library["Books"].pop(book)
                return f"{book_name} is deleted from books library"
            ## Todo : Find a way to delete book by his name (should delete all books details)
            else:
                print(f"The book {book_name} does not exist!")
            if identifier == 'n':
                print("Canceling...")
                break
