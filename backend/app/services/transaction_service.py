import pandas as pd
from datetime import datetime
from app.models.transaction import Transaction
from app.repositories.transactionRepo import transactionRepo

class TransactionService:
    def __init__(self, transaction_repo: transactionRepo):
        self.transaction_repo = transaction_repo

    def add_transaction(self, description, category, subcategory, amount):
        # Automatically treat the amount as negative if it's an expense
        if category == "Expense" and amount > 0:
            amount = -amount  # Ensure that the amount is negative for expenses
        elif category == "Income" and amount < 0:
            amount = -amount  # Ensure that the amount is positive for income

        # Get date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add transaction, including category and subcategory
        transaction = Transaction(current_datetime, description, category, subcategory, amount)
        self.transaction_repo.add_transaction(transaction)
        
    def get_transactions(self):
        return self.transaction_repo.get_transactions()

    def calculate_totals(self):
        transactions = self.get_transactions()
        income = sum(t[5] for t in transactions if t[3] == "Income")
        expenses = sum(t[5] for t in transactions if t[3] == "Expense")
        return income, expenses

    def export_transactions_to_csv(self, file_name='transactions.csv'):
        transactions = self.get_transactions()
        # Ensure data has the correct number of columns, including subcategory
        df = pd.DataFrame(transactions, columns=["ID", "Date", "Description", "Category", "Subcategory", "Amount"])
        df.to_csv(file_name, index=False, float_format='%.2f')