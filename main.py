from admin import Admin

def user_menu(user):
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            user.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            user.withdraw(amount)
        elif choice == "3":
            print("Current Balance:", user.check_balance())
        elif choice == "4":
            print("Transaction History:")
            for transaction in user.check_transaction_history():
                print(transaction)
        elif choice == "5":
            amount = float(input("Enter loan amount: "))
            user.take_loan(amount)
        elif choice == "6":
            recipient_account_number = input("Enter recipient account number: ")
            recipient = admin.find_user_by_account_number(recipient_account_number)
            if recipient:
                amount = float(input("Enter transfer amount: "))
                user.transfer(amount, recipient)
            else:
                print("Recipient account not found.")
        elif choice == "7":
            print("Exiting user menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. List Accounts")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings / Current): ")
            admin.create_account(name, email, address, account_type)
        elif choice == "2":
            account_number = input("Enter account number to delete: ")
            user_to_delete = admin.find_user_by_account_number(account_number)
            if user_to_delete:
                admin.delete_account(user_to_delete)
            else:
                print("User not found.")
        elif choice == "3":
            admin.list_accounts()
        elif choice == "4":
            print("Total Available Balance:", admin.total_available_balance())
        elif choice == "5":
            print("Total Loan Amount:", admin.total_loan_amount())
        elif choice == "6":
            status = input("Enter 'on' to enable loan feature or 'off' to disable: ").lower()
            if status == "on":
                admin.toggle_loan_feature(True)
            elif status == "off":
                admin.toggle_loan_feature(False)
            else:
                print("Invalid choice.")
        elif choice == "7":
            print("Exiting admin menu.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    admin = Admin()
    while True:
        print("\nWelcome to the banking management system!")
        print("Select user type:")
        print("1. User")
        print("2. Admin")
        print("3. Exit")

        user_type = input("Enter your choice: ")

        if user_type == "1":
            print("\nUser Menu:")
            account_type = input("Enter your account type (Savings / Current): ")
            user = admin.create_account(input("Enter your name: "), input("Enter your email: "), input("Enter your address: "), account_type)
            user_menu(user)
        elif user_type == "2":
            admin_menu(admin)
        elif user_type == "3":
            print("Exiting the banking management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")