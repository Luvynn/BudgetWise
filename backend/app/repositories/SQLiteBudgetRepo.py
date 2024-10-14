import sqlite3
from app.models.budget import Budget
from app.repositories.budgetRepo import BudgetRepository

class SQLiteBudgetRepository(BudgetRepository):
    def __init__(self, db_path=":memory:"):
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS budgets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    amount REAL
                )
                """
            )

    def add_budget(self, budget: Budget):
        with self.connection:
            self.connection.execute(
                "INSERT INTO budgets (category, amount) VALUES (?, ?)",
                (budget.category, budget.amount)
            )

    def get_budgets(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM budgets")
        return cursor.fetchall()
