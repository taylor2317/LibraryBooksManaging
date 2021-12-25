from datetime import datetime
import math
import json
import pickle
from LibraryBooks import *
from LibraryCustomers import *
from main import *
# This script will handle the loan system, while receiving data from librarybooks and librarycustomers

class Loans:
    """
    A class that represents the loan system of the library
    while receiving customers data and books data from the library
    """
    
    def __init__(self,loan_custID,loan_bookID,loan_date,loan_return_date):
        """
        :param loan_custID: The customer's ID
        :param loan_bookID: The book's ID
        :param loan_date: The date that the customer took the book
        :param loan_return_date: The date that the customer returned the book
        """
        self.loan_custID = loan_custID
        self.loan_bookID = loan_bookID
        self.loan_date = loan_date
        self.loan_return_date = loan_return_date

loan_library = {"Customer":{
                            "Customer's ID":{}}}
late_loans = {"Customer":{
                        "Customer's ID":{}}}
blacklist = []

date_format = "%d/%m/%Y"

def loan_a_book(loan_custID,loan_bookID,loan_date):
    # the function checks if the customer is in the customers list,
    # also checks if customer has a loan already
    # customer can loan a book only if he is not currently has a loan.
    if find_book_by_name(book_name_input, books_library) == True:
        for book in books_library["Books"]:
            if loan_bookID in books_library["Books"][book]["Book's copies"]:
                if books_library["Books"][book]["Book's copies"] <= 0:
                    print(f"Book: '{book_name_input}' has: '{book_copies}' in the library currently.")
                else:
                    print(f"Do you want to loan '{book_name_input}' ?\n \
                            1. Yes \n \
                                2. No")
                    identifier = input()
                    identifiers = ['1','2']
                    while identifier not in identifiers:
                        print("Invalid identifier please select one from the Menu")
                        print(f"Do you want to loan '{book_name_input}' ?\n \
                            1. Yes \n \
                                2. No")
                        identifier = input()
                    if identifier == '1': # Choosing to loan the book
                        books_library["Books"][book]["Books's copies"] -= 1
                        for customer in customers_library["Customers"]:
                            if loan_custID in customers_library["Customers"][customer]["Customer's ID"]:
                                loan_library["Customer"]["Customer's ID"].update(loan_custID)
                                loan_library["Customer"]["Customer's ID"][loan_custID]["Book's ID"] = books_library["Books"][book]["Book's ID"]
                                loan_library["Customer"]["Customer's ID"][loan_custID]["loan date"] = datetime.strptime(loan_date, date_format)
                                                    #loan_library["Customer"]["Customer's ID"][loan_custID]["loan return date"] = datetime.strptime(loan_return_date, date_format)
                                if books_library["Books"][book]["Book's type"] == '1':
                                    print(f"You've loan '{book_name_input}' successfully!\n \
                                        Since it's type '1' book you should return this book in '10' days to avoid punishment (;")
                                    continue
                                if books_library["Books"][book]["Book's type"] == '2':
                                    print(f"You've loan '{book_name_input}' successfully!\n \
                                        Since it's type '2' book you should return this book in '5' days to avoid punishment (;")
                                    continue
                                if books_library["Books"][book]["Book's type"] == '3':
                                    print(f"You've loan '{book_name_input}' successfully!\n \
                                        Since it's type '3' book you should return this book in '2' days to avoid punishment (;")
                                    continue
                    if identifier == '2': # Choosing not to loan the book
                        print("Going back...")
                        break
                    print("successfully loaned a book function")
                ### TODO : to check how many copies the book have, and -1 if it has more than 0
                    #loan_library["Customer"]["Customer's ID"][loan_custID]["loan return date"] = datetime.strptime(loan_return_date, date_format)

def return_a_book(loan_custID,loan_bookID,loan_return_date):
    if find_book_by_name(book_name_input, books_library) == True:
        for book in books_library["Books"]:
            if loan_bookID in books_library["Books"][book]["Book's copies"]:
                if books_library["Books"][book]["Book's copies"] <= 0:
                    print(f"Book: '{book_name_input}' has: '{book_copies}' in the library currently.")
                else:
                    loan_custID = input("Enter your ID: ")
                    if loan_custID in loan_library["Customers"]["Customer's ID"]:
                        loan_library["Customer"]["Customer's ID"][loan_custID]["loan returned date"] = datetime.strptime(loan_return_date, date_format)
                        if books_library["Books"][book]["Book's type"] == '1':
                            if loan_library["Customer"]["Customer's ID"][loan_custID]["loan returned date"] - loan_library["Customer"]["Customer's ID"][loan_custID]["loan date"] > 10:
                                print("you are gonna be punished !! ")
                                late_loans.update(loan_library["Customer"]["Customer's ID"][loan_custID]["late loan": {loan_library["Customer"]["Customer's ID"][loan_custID]["loan returned date"] - loan_library["Customer"]["Customer's ID"][loan_custID]["loan date"]}])
                            else:
                                loan_library["Customer"]["Customer's ID"].pop(loan_custID)
                                print("Returned the book before the '10' days of loan over...thank you")
                                
                        if books_library["Books"][book]["Book's type"] == '2':
                            if loan_library["Customer"]["Customer's ID"][loan_custID]["loan returned date"] - loan_library["Customer"]["Customer's ID"][loan_custID]["loan date"] > 5:
                                print("you are gonna be punished !! ")
                                late_loans.update(loan_library["Customer"]["Customer's ID"][loan_custID]["late loan": {loan_library["Customer"]["Customer's ID"][loan_custID]["loan returned date"] - loan_library["Customer"]["Customer's ID"][loan_custID]["loan date"]}])

                            else:
                                loan_library["Customer"]["Customer's ID"].pop(loan_custID)
                                print("Returned the book before the '5' days of loan over...thank you")
                                
                        if books_library["Books"][book]["Book's type"] == '3':
                            if loan_library["Customer"]["Customer's ID"][loan_custID]["loan returned date"] - loan_library["Customer"]["Customer's ID"][loan_custID]["loan date"] > 2:
                                print("you are gonna be punished !! ")
                                late_loans.update(loan_library["Customer"]["Customer's ID"][loan_custID]["late loan": {loan_library["Customer"]["Customer's ID"][loan_custID]["loan returned date"] - loan_library["Customer"]["Customer's ID"][loan_custID]["loan date"]}])
                            else:
                                loan_library["Customer"]["Customer's ID"].pop(loan_custID)
                                print("Returned the book before the '2' days of loan over...thank you")
                                
def display_all_loans(loan_library):
    return loan_library

def display_all_late_loans(late_loans):
    return late_loans

