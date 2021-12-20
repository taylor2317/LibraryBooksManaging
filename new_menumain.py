from LibraryBooks import *
from LibraryCustomers import *
from LibraryLoan import *
import json

books_library = []
main_menu = "Main Menu: \n\n \
                        1. Books Menu.\n \
                            2. Customers Menu.\n \
                                3. Loan Menu.\n \
                                    4. Exit."
books_menu = "Books Menu: \n\n \
                        1. Add a new book. \n \
                            2. Display all books. \n \
                                3. Find a book (by name). \n \
                                    4. Remove a book. \n \
                                        5. Back."
customers_menu = "Customers Menu: \n\n \
                            1. Add a new customer.\n \
                                2. Display all customers.\n \
                                    3. Find a customer (by name). \n \
                                        4. Remove a customer. \n \
                                            5. Back"
loan_menu = "Loan Menu: \n\n \
                        1. Loan a book.\n \
                            2. Return a Book.\n \
                                3. Display all Loans.\n \
                                    4. Display 'Late' loans.\n \
                                        5. Display loans (by customer).\n \
                                            6. Display loans (by book)\n \
                                                7. Back."
if __name__ == '__main__':
    while True: # The script will be running until "Exit" is selected from the Main Menu
        print(main_menu)
        print("Choose books/customers/loans menu: ")
        identifier = input()
        identifiers = ['1','2','3','4']
        while identifier not in identifiers:
            print("Invalid identifier please select one from the Menu")
            print(main_menu)
            identifier = input()
        if identifier == '1': # Choosing books Menu
            while True: # books menu keeps runing until "Back" will be selected from books menu
                print(books_menu)
                print("What would you like to do?: ")
                identifiers = ['1','2','3','4','5']
                identifier = input()
                while identifier not in identifiers:
                    print("Invalid identifier please select one from the Menu")
                    print(books_menu)
                    identifier = input()
                if identifier == '1': # Choosing to add new book
                    print("Adding a new book: ")
                    book_id = input("Enter book's ID:")
                    book_name = input("Enter book's name: ")
                    book_author = input("Enter book's author: ")
                    book_published_year = input("Enter book's published year: ")
                    book_type = input("Enter book's type: ")
                    book_type_options = ['1','2','3'] # 1 = 10 days rental, 2 = 5 days rental, 3 = 2 days rental
                    while book_type not in book_type_options:
                        print("Invalid book type, try again!")
                        book_type = input("Enter book's type: ")
                    book_copies = input("Enter book's number of copies: ")
                    new_book = add_new_book(book_id, book_name, book_author, book_published_year,book_type,book_copies)
                    books_library.append(new_book)
                    print(books_library)
                    continue
                if identifier == '2': # Choosing to Display all books
                    print("All the books that in the library: ")
                    print(display_all_books(books_library))
                if identifier == '3': # Choosing to Find a book (by name)
                    print("Which book would you like to find?\n \
                            Enter book's name: ")
                    book_name = input()
                    find_book = find_book_by_name(book_name, books_library)
                    print(find_book)
                    continue