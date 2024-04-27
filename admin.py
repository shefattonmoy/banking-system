from user import User

class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        print("Account created successfully. Account number:", user.account_number)
        return user

    def delete_account(self, user):
        self.users.remove(user)
        print("Account deleted successfully.")

    def list_accounts(self):
        for user in self.users:
            print("Name:", user.name, "Email:", user.email, "Account Type:", user.account_type, "Balance:", user.balance)

    def total_available_balance(self):
        total_balance = sum(user.balance for user in self.users)
        return total_balance

    def total_loan_amount(self):
        total_loan = sum(user.balance for user in self.users if user.account_type == 'Loan')
        return total_loan

    def toggle_loan_feature(self, status):
        if status:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")
    
    def find_user_by_account_number(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None