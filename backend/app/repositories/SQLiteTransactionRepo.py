# backend/app/repositories/SQLiteTransactionRepository.py

import sqlite3
from app.models.transaction import Transaction
from app.repositories.transactionRepo import transactionRepo

class SQLiteTransactionRepository(transactionRepo):
    def __init__(self, db_path=":memory:"):
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()
    
    def create_table(self):
        with self.connection:
            self.connection.execute("DROP TABLE IF EXISTS transactions")  # Drop the table if it exists
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    description TEXT,
                    category TEXT,
                    subcategory TEXT, 
                    amount REAL
                )
                """
            )

    def add_transaction(self, transaction: Transaction):
        with self.connection:
            self.connection.execute(
                "INSERT INTO transactions (date, description, category, subcategory, amount) VALUES (?, ?, ?, ?, ?)",
                (transaction.date, transaction.description, transaction.category, transaction.subcategory, transaction.amount)
            )

    def get_transactions(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM transactions")
        return cursor.fetchall()
