class Customer:
    def __init__(self, name, customer_id, password="", balance=0):
        self.name = name
        self.customer_id = customer_id
        self.balance = balance
        self.password = password

def new_customer():
    name = input("Enter the name: ")
    customer_id = input("Enter your customer ID: ")
    password = input("Set your password: ")

    if customer_id in customers:
        print("Customer ID already exists. Please choose a different ID.")
    else:
        try:
            balance = int(input("Enter the initial balance: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for the balance.")
            return  # Exit the function in case of an error
        customers[customer_id] = Customer(name, customer_id, password,balance)
        print("Account created successfully.")

def deposit(customer, amount):
    if amount > 0:
        customer.balance += amount
        print("Balance is:", customer.balance)
    else:
        print("Please enter a positive amount to deposit.")

def withdrawal(customer, amount):
    if amount > 0:
        if amount <= customer.balance:
            customer.balance -= amount
            print("Balance is:", customer.balance)
        else:
            print("Insufficient balance.")
    else:
        print("Please enter a positive amount to withdraw.")

def check_balance(customer):
    print("Your current Balance is:", customer.balance)

# Create instances for each customer
customers = {
    "3231567": Customer("ABHIDHA RAJAN", "3231567", "Sreedath@21", 50000),
    "3231789": Customer("UPAMA RAJAN", "3231789", "Aditikris123", 100000),
    "3231234": Customer("AKHILA RAJAN", "3231234", "Nakshathra!04", 75000)
}

# Main program
print("$$***$$ WELCOME TO ABC BANK $$***$$")
print("1. Create an account")
print("2. Existing customer login")
choice = input("Enter the option")

if choice == "1":
    new_customer()
elif choice == "2":
    while True:
        U = input('Enter the Username: ')
        P = input("Enter the password: ")

        if U in customers and customers[U].password == P:
            print('Successfully logged in')
            print("WELCOME", customers[U].name)

            # Banking operations
            while True:
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdrawal")
                print("4. Logout")
                option = input("Enter the option: ")

                if option == '1':
                    check_balance(customers[U])
                elif option == '2':
                    amount = float(input("Enter the amount to deposit: "))
                    deposit(customers[U], amount)
                elif option == '3':
                    amount = float(input("Enter the amount to withdraw: "))
                    withdrawal(customers[U], amount)
                elif option == '4':
                    print("Thank you for using ABC Banking System.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            break
        else:
            print("Invalid username or password. Please try again.")
else:
    print("Please enter a correct option")
