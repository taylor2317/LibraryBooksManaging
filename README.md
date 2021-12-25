# LibraryBooksManaging
I have a project
In this project I need to implement a simple system to manage books library.
My system should be able to manage the following entities:
- Books
- Customers
- Loans

Each entity has a menu:

Main menu:
1. books menu:
    1. add book      
      2. display all book      
        3. find book (by name)      
          4. remove book (by name)

2. customers menu:
    1. add customer
      2. display all customers 
        3. find customer (by name) 
          4. remove customer

3. loan menu:
     1. loan book   =   (by book name that return the book id to the loan library
                           And by the customer name that returns customer's id to the loan library)
       2. return book  =  (by book's name that add the date of returned book,
                             And by customer's name that checks if the customer 
                             returned the book in time depends on book's type : 1 = 10 days rental, 2 = 5 days rental , 3 = 2 days rental)
                                    Return book function will add to late_loans(dictionary) the customer if the customer didn't return book on time
                                        (with doing so, when ever the customer want to rent book again, he will have to wait 2 weeks as punishment.)
              3. display all loans (shows all the loans in library)
                4. display all late loans (shows all the late loans by customer id, and the reason he's there)
                  5. display loans (by customer's name, if in late loans - will show the late loan)
                    6. display loans (by book)

