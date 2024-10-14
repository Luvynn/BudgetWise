import os
import unittest
from datetime import datetime

# Correct import paths based on directory structure
from app.services.transaction_service import TransactionService
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        # Use an in-memory SQLite database for testing
        self.repo = SQLiteTransactionRepository(":memory:")  
        self.service = TransactionService(self.repo)

    def test_add_transaction(self):
        self.service.add_transaction("Salary", "Income", "Salary", 1000)
        transactions = self.service.get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][2], "Salary")
        self.assertEqual(transactions[0][3], "Income")
        self.assertEqual(transactions[0][4], "Salary")  # Check subcategory
        self.assertEqual(transactions[0][5], 1000)
        # Check that the date is automatically added (not None)
        self.assertIsNotNone(transactions[0][1])

    def test_get_transactions(self):
        self.service.add_transaction("Salary", "Income", "Salary", 1000)
        self.service.add_transaction("Groceries", "Expense", "Food", 200)
        transactions = self.service.get_transactions()
        self.assertEqual(len(transactions), 2)

    def test_calculate_totals(self):
        self.service.add_transaction("Salary", "Income", "Salary", 1000)
        self.service.add_transaction("Groceries", "Expense", "Food", 200)
        income, expenses = self.service.calculate_totals()
        self.assertEqual(income, 1000)
        self.assertEqual(expenses, -200)

    def test_export_transactions_to_csv(self):
        # Add transactions
        self.service.add_transaction("Salary", "Income", "Salary", 1000)
        self.service.add_transaction("Groceries", "Expense", "Food", 200)

        # Export to CSV
        file_name = "test_transactions.csv"
        self.service.export_transactions_to_csv(file_name)

        # Check if the file exists
        self.assertTrue(os.path.exists(file_name))

        # Verify file content
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 3)  # Header + 2 transactions
            
            # Check the first transaction line, using the actual date when the transaction was added
            expected_date_1 = datetime.now().strftime("%Y-%m-%d")  # Only check the date part
            self.assertTrue(lines[1].startswith(f"1,{expected_date_1}"))
            self.assertIn("Salary,Income,Salary,1000.00", lines[1])
            
            # Check the second transaction line
            expected_date_2 = datetime.now().strftime("%Y-%m-%d")
            self.assertTrue(lines[2].startswith(f"2,{expected_date_2}"))
            self.assertIn("Groceries,Expense,Food,-200.00", lines[2])
        
        # Clean up
        os.remove(file_name)
        
if __name__ == "__main__":
    unittest.main()
