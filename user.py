import uuid
from datetime import datetime

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = str(uuid.uuid4())
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append((datetime.now(), 'Deposit', amount))
        print("Deposit successful. Current balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append((datetime.now(), 'Withdrawal', amount))
            print("Withdrawal successful. Current balance:", self.balance)
        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.balance += amount
            self.loan_taken += 1
            self.transaction_history.append((datetime.now(), 'Loan', amount))
            print("Loan taken successfully. Current balance:", self.balance)
        else:
            print("You can't take more loans.")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            recipient.deposit(amount)
            self.withdraw(amount)
            print("Transfer successful")
        else:
            print("Insufficient funds")