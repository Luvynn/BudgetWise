import unittest
import os
from datetime import datetime

from app.services.budget_service import BudgetService
from app.repositories.SQLiteBudgetRepo import SQLiteBudgetRepository
from app.services.transaction_service import TransactionService
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        # Use in-memory SQLite databases for testing
        self.budget_repo = SQLiteBudgetRepository(":memory:")
        self.transaction_repo = SQLiteTransactionRepository(":memory:")
        self.transaction_service = TransactionService(self.transaction_repo)
        self.budget_service = BudgetService(self.budget_repo, self.transaction_service)

    def test_add_budget(self):
        self.budget_service.add_budget("Food", 500)
        budgets = self.budget_service.get_budgets()
        self.assertEqual(len(budgets), 1)
        self.assertEqual(budgets[0][1], "Food")
        self.assertEqual(budgets[0][2], 500)

    def test_get_budgets(self):
        self.budget_service.add_budget("Food", 500)
        self.budget_service.add_budget("Entertainment", 200)
        budgets = self.budget_service.get_budgets()
        self.assertEqual(len(budgets), 2)

    def test_compare_budget(self):
        # Add budgets
        self.budget_service.add_budget("Food", 500)
        self.budget_service.add_budget("Entertainment", 200)
        
        # Add transactions with specific categories and subcategories
        self.transaction_service.add_transaction("Grocery Shopping", "Expense", "Food", 150)
        self.transaction_service.add_transaction("Movie Ticket", "Expense", "Entertainment", 50)
        
        # Get the comparison
        comparison = self.budget_service.compare_budget()
        
        # Test the comparison results
        food_comparison = comparison["Food"]
        entertainment_comparison = comparison["Entertainment"]

        self.assertEqual(food_comparison["budgeted"], 500)
        self.assertEqual(food_comparison["spent"], 150)
        self.assertEqual(food_comparison["remaining"], 350)

        self.assertEqual(entertainment_comparison["budgeted"], 200)
        self.assertEqual(entertainment_comparison["spent"], 50)
        self.assertEqual(entertainment_comparison["remaining"], 150)

    def test_export_budgets_to_csv(self):
        # Add budgets
        self.budget_service.add_budget("Food", 500)
        self.budget_service.add_budget("Entertainment", 200)
        
        # Add transactions
        self.transaction_service.add_transaction("Grocery Shopping", "Expense", "Food", 150)
        self.transaction_service.add_transaction("Movie Ticket", "Expense", "Entertainment", 50)
        
        # Export to CSV
        file_name = "test_budgets_export.csv"
        self.budget_service.export_budgets_to_csv(file_name)
        
        # Check if the file exists
        self.assertTrue(os.path.exists(file_name))
        
        # Verify file content
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 3)  # Header + 2 budgets
            self.assertEqual(lines[0].strip(), "Category,Budgeted,Spent,Remaining")
            self.assertEqual(lines[1].strip(), "Food,500.00,150.00,350.00")
            self.assertEqual(lines[2].strip(), "Entertainment,200.00,50.00,150.00")

            # Clean up
            # os.remove(file_name)

if __name__ == "__main__":
    unittest.main()