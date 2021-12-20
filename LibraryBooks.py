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
    

def add_new_book(book_id,book_name,book_author,book_published_year,book_type,book_copies):
    new_book = ["book's ID", #:book_id,
                    "book's Name",#:book_name,
                    "book's Authors",#:book_author,
                    "book's Published year",#:book_published_year,
                    "book's Type",#:book_type,
                    "book's Copies"]#:book_copies]
    new_book["book's ID"].append(book_id)
    new_book["book's Name"].append(book_name)
    new_book["book's Authors"].append(book_author)
    new_book["book's Published year"].append(book_published_year)
    new_book["book's Type"].append(book_type)
    new_book["book's Copies"].append(book_copies)
    return  new_book

def display_all_books(books_library):
    """
    :return: all the books in the books, library
    """
    return books_library
    
def find_book_by_name(book_name, books_library):
    """
    A search function for searching books in the library by their names
    :param book_name: The name of the book to search
    :param book_library: All the books in library"""
        
    books_library_temp = copy.deepcopy(books_library)
    if book_name in books_library_temp.keys():
        for book in books_library_temp[book_name]:
            books_library_temp[book_name] = books_library_temp[book]
            return books_library_temp[book]
    else:
        return f"There is no such {book_name} book in the library."
    
def delete_book(book_name, books_library={}):
    """
    A function that update the collection of books that in the library, without deleting one.
    :param book_name: The name of the book to delete.
    :param books_library: A collection of all the books in library
    """
    if book_name in books_library:
        print(f"The book {book_name} has deleted from library")
        books_library.pop(book_name)
    else:
        print(f"The book {book_name} does not exist!")
    