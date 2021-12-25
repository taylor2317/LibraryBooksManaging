# imports:
import copy
import LibraryLoan
import LibraryBooks
import json
import pickle

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
    
    
    def __str__(self):
        return f"{self.customer_id},{self.customer_name},{self.customer_city},{self.customer_age}"
    
customers_library = {"Customers": []}

def add_new_customer(customer_id, customer_name, customer_city, customer_age):
    """
    A function that add new customer to the Library
    :param customer_id: Customer's ID'
    :param customer_name: Customer's name'
    :param customer_city: Customer's city'
    :param customer_age: Customer's age'
    """
    #todo: try different method that can return dict. return customers_library["Customers"].append({"Customer's ID":customer_id,"Customer's Name":customer_name,"Customer's City":customer_city,"Customer's age":customer_age})
        
    new_customer = customers_library["Customers"].append({"Customer's ID":customer_id,"Customer's Name":customer_name,"Customer's City":customer_city,"Customer's age":customer_age})
    
    with open('customers_data.pkl', 'wb') as customer_save:
        pickle.dump(customers_library, customer_save)
         
    return new_customer
    
    
def display_all_customers(customers_library):
    """
    A function that returns all the customers in the library
    """
    with open('customers_data.pkl', 'rb') as c_read:
        customers_library = pickle.load(c_read)
        
    return customers_library
   
   
    
def find_customer_by_name(customer_name, customers_library):
    """
    A search function that search customer in library by his name
    :param customer_name: Customer's name'
    :param customers_library: a dict with all customers in the library
    """
    for customer in range(len(customers_library["Customers"])):
        if customer_name in customers_library["Customers"][customer]["Customer's Name"]:
            return f"The customer: '{customer_name}' is in the library"
    else:
        return f"There is no customer named: '{customer_name}' in the library"
    
    # for customer in range(len(customers_library["Customers"])):
    #     if customer_name in customers_library["Customers"][customer]["Customer's Name"]:
    #         return f"The customer: '{customer_name}' is in the library"
    #         #return f"Details of {customer_name}:\n Customer's ID: {customer_id}\nCustomer's City: {customer_city}\nCustomer's age: {customer_age}"
    #     else:
    #         return f"There is no customer named: '{customer_name}' in the library"

        
def remove_customer(customer_name, customers_library):
   # customer can be removed only if he returned all the books he rented. customer num of books should be 0.
        for customer in range(len(customers_library["Customers"])):
            if customer_name in customers_library["Customers"][customer]["Customer's Name"]:
                print(f"Are you sure you want delete customer: '{customer_name}' from the library?, y/n: ")
                identifier = input()
                identifiers = ['y','n']
                while identifier not in identifiers:
                    print("Please answer with y or n")
                    print(f"Are you sure you want delete customer: '{customer_name}' from the library?, y/n: ")
                    identifier = input()
                if identifier == 'y':
                    customers_library["Customers"].pop(customer)
                    with open('customers_data.pkl', 'wb') as c_output_new_customer:
                        pickle.dump(customers_library, c_output_new_customer)
                    return f"The customer: {customer_name} is deleted from the library successfully!"
                else:
                    print(f"The customer: {customer_name} does not exist!")
                if identifier == 'n':
                    print("Canceling...")
                    break
