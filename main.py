from LibraryBooks import *
from LibraryCustomers import *
from LibraryLoan import *
import json
import datetime


with open('customers_data.pkl', 'rb') as c_read:
        customers_library = pickle.load(c_read)

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
    while True:  # The script will be running until "Exit" is selected from the Main Menu
        print(main_menu)
        print("Choose books/customers/loans menu: ")
        identifier = input()
        identifiers = ['1', '2', '3', '4']
        while identifier not in identifiers:
            print("Invalid identifier please select one from the Menu")
            print(main_menu)
            identifier = input()
        if identifier == '1':  # Choosing books Menu
            while True:  # books menu keeps runing until "Back" will be selected from books menu
                print(books_menu)
                print("What would you like to do?: ")
                identifiers = ['1', '2', '3', '4', '5']
                identifier = input()
                while identifier not in identifiers:
                    print("Invalid identifier please select one from the Menu")
                    print(books_menu)
                    identifier = input()
                if identifier == '1':  # Choosing to add new book
                    print("Adding a new book: ")
                    book_id = input("Enter book's ID:")
                    book_name = input("Enter book's name: ")
                    book_author = input("Enter book's author: ")
                    book_published_year = input("Enter book's published year: ")
                    book_type = input("Enter book's type: ")
                    book_type_options = ['1', '2', '3']  # 1 = 10 days rental, 2 = 5 days rental, 3 = 2 days rental
                    while book_type not in book_type_options:
                        print("Invalid book type, try again!")
                        book_type = input("Enter book's type: ")
                    book_copies = int(input("Enter book's number of copies: "))
                    new_book = add_new_book(book_id, book_name, book_author, book_published_year,
                                            book_type, book_copies)
                    # books_library.append(new_book)
                    print(books_library)
                    continue
                if identifier == '2':  # Choosing to Display all books
                    print("All the books that in the library: ")
                    print(display_all_books(books_library))
                    continue
                if identifier == '3':  # Choosing to Find a book (by name)
                    print("Which book would you like to find?\n \
                            Enter book's name: ")
                    book_name = input()
                    find_book = find_book_by_name(book_name, books_library)
                    print(find_book)
                    continue
                if identifier == '4':  # choosing to Remove a book
                    print("Which book would you like to remove?: \n")
                    book_name = input()
                    delete_book(book_name, books_library)
                    print("The Book has deleted from library.")
                    continue
                if identifier == '5':  # Choosing to go Back
                    print("going back to main menu")
                    break
                continue
        if identifier == '2':  # Choosing the Customers menu
            while True: # The Customers menu will running until 'Back' will be selected from the menu
                print(customers_menu)
                print("What would you like to do?: ")
                identifiers = ['1', '2', '3', '4', '5']
                identifier = input()
                while identifier not in identifiers:
                    print("Invalid identifier please select one from the Menu")
                    print(customers_menu)
                    identifier = input()
                if identifier == '1':  # Choosing to add customer
                    print("Adding a customer:")
                    customer_id_input = input("Enter customer's ID: ")
                    customer_name_input = input("Enter customer's name: ")
                    customer_city_input = input("Enter customer's city: ")
                    customer_age_input = input("Enter customer's age: ")
                    new_customers = add_new_customer(customer_id_input, customer_name_input,
                                                              customer_city_input, customer_age_input)
                    print("Added customer...")
                    print("Done!, Customer added successfully")
                    print(f"\n{customers_library}\n\n")
                    continue
                if identifier == '2':  # Choosing to display all customers
                    print("Display all customers in the library: ")
                    print(display_all_customers(customers_library))
                    continue
                if identifier == '3':  # Choosing to find customer (by name)
                    print("Enter customer's name you would like to find: ")
                    customer_name = input()
                    find_customer = find_customer_by_name(customer_name, customers_library)
                    print(find_customer)
                    continue
                if identifier == '4':  # Choosing to delete a customer (by name)
                    print("Which customer would you like to remove?: \n")
                    customer_name = input()
                    remove_customer(customer_name, customers_library)
                    print(f"The customer: '{customer_name}' was removed from the library successfully.....")
                if identifier == '5': # Choosing to go Back to Main Menu
                    print("going back to main menu")
                    break
                continue
        if identifier == '3': # Choosing Loan Menu
            while True: # Loan menu will running until 'Back' will be selected from the menu
                print(loan_menu)
                print("What would you like to do?:")
                identifier = input()
                identifiers = ['1', '2', '3', '4','5','6','7']
                while identifier not in identifiers:
                    print("Invalid identifier please select one from the Menu")
                    print(loan_menu)
                    identifier = input()
                if identifier == '1': # Choosing to loan a book
                    custoer_id_input = input("Enter your ID: ")
                    book_name_input = input("Enter Books name: ")
                    book_id = input("Enter book ID: ")
                    loan_a_book(custoer_id_input,book_id,loan_date=datetime.date.today())
                    print("Book loaned to you!!!")
                if identifier == '2': # Choosing to return a book
                    pass
                if identifier == '3': # Choosing to display all loans
                    pass
                if identifier == '4': # Choosing to display 'late' loans
                    pass
                if identifier == '5': # Choosing to display loans (by customer)
                    pass
                if identifier == '6': # Choosing to display loans (by book)
                    pass
                if identifier == '7': # Choosing to go back to Main menu
                    print("Going back to Main Menu...")
                    break
            continue
        if identifier == '4': # Choosing to exit the program
            print("Goodbye!")
            exit()
            
            
