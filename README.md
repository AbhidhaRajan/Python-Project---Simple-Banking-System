Link to view my Video presentation on Google Drive:https://drive.google.com/file/d/1saDo9KVkkzi2iCtW4186_rxJgcrxDjGS/view?usp=drive_link



# Python-Project---Simple-Banking-System
 This project aims to create a command-line-based banking system that allows users to create customer accounts, log in, and perform basic banking operations. The system is designed with simplicity in mind, and it serves as a starting point for a more comprehensive banking application.
## Code Explanation:
The project comprises the following components:
## Customer Class (class Customer):
The Customer class represents customer accounts. Each customer is identified by a unique customer ID and has attributes such as name, balance, and password. The __init__ method serves as the constructor for creating customer objects with these attributes.
## Functions:
## new_customer(): This function allows a user to create a new customer account. It prompts the user for their name, customer ID, password, and initial balance. The function checks if the customer ID is already in use and, if not, creates a new customer object and adds it to the customers dictionary.
## deposit(customer, amount): This function lets a customer deposit money into their account. It takes a customer object and an amount as parameters, and it updates the customer's balance.
## withdrawal(customer, amount): This function permits customers to withdraw money from their account. It checks if the amount is valid and if the customer has sufficient balance.
## check_balance(customer): This function displays the balance of a specific customer.
## customers Dictionary:
The customers dictionary stores customer objects with customer IDs as keys. 
### Main Program:
The main program starts with a welcome message and presents two menu options:
"Create an account" (Option 1) - This allows new customers to create an account using the new_customer() function.
"Existing customer login" (Option 2) - Existing customers can log in and access their accounts.
If the user chooses to log in, they are prompted to enter a username and password. The code checks if the credentials are correct by verifying them against the stored customer data.
Upon successful login, the user is presented with banking operation choices such as checking their balance, depositing money, and withdrawing money.
The program loops through the banking operations until the user decides to log out.
If the user enters incorrect credentials or an invalid option, appropriate error messages are displayed.


