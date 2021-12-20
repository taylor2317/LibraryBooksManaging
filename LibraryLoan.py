import datetime
import math
import json
import pickle
from LibraryBooks import *
from LibraryCustomers import *
# This script will handle the loan system, while receiving data from librarybooks and librarycustomers

class Loans:
    """
    A class that represents the loan system of the library
    while receiving customers data and books data from the library
    """
    
    def __init__(self,loan_custID,loan_bookID,loan_date,loan_return_date):
        """
        """