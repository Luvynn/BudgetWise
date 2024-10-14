# backend/app/models/transaction.py

class Transaction:
    def __init__(self, date, description, category, subcategory, amount):
        self.date = date
        self.description = description
        self.category = category  # Income or Expense
        self.subcategory = subcategory  # Specific budget category like Food, Entertainment, etc.
        self.amount = amount
