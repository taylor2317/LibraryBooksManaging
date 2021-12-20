# imports:
import copy
import LibraryLoan
import LibraryBooks

# This script will contain the customers functions

class Customer:
    """
    A class that represents the Customer object
    """
    
    def __init__(self,customer_id,customer_name,customer_city,customer_age):
        """
        A function that contains all the relevant information of customers
        :param customer_id: Customer's ID
        :param customer_name: Customer's name
        :param customer_city: Customer's city of living
        :param customer_age: Customer's age'
        """
        
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_city = customer_city
        self.customer_age = customer_age
    
        self.customers_library = {'customer id': {},
                         'customer name': {},
                         'customer city': {},
                         'customer age': {}}
    
    
    def __str__(self):
        return f"{self.customer_id},{self.customer_name},{self.customer_city},{self.customer_age}"
    
    
    def add_new_customer(customer_id, customer_name, customer_city, customer_age):
        """
        A function that add new customer to the Library
        :param customer_id: Customer's ID'
        :param customer_name: Customer's name'
        :param customer_city: Customer's city'
        :param customer_age: Customer's age'
        """
        new_customer = {'customer id':customer_id,
                        'customer name':customer_name,
                        'customer city':customer_city,
                        'customer age':customer_age }
        return new_customer
    
    def display_all_customers(self,customers_library):
        """
        A function that returns all the customers in the library
        """
        return customers_library
    
    def find_customer_by_name(self,customer_name, customers_library):
        """
        A search function that search customer in library by his name
        :param customer_name: Customer's name'
        :param customers_library: a dict with all customers in the library
        """
        customers_temp_library = copy.deepcopy(customers_library)
        if customer_name in customers_temp_library.keys():
            for customer in customers_library[customer_name]:
                customers_temp_library[customer_name] = customers_temp_library[customer]
                return customers_temp_library[customer]
        else:
            return f"There are no customer named: {customer_name} in the library"
        
    def remove_customer(customer_name, customers_library):
        # customer can be removed only if he returned all the books he rented. customer num of books should be 0.
        pass

# def add_new_customer(customer_id, customer_name, customer_city, customer_age):
#     """
#     A function that add new customer to the Library
#     :param customer_id: Customer's ID'
#     :param customer_name: Customer's name'
#     :param customer_city: Customer's city'
#     :param customer_age: Customer's age'
#     """
#     new_customer = Customer(customer_id, customer_name,customer_city,customer_age)
#     return new_customer