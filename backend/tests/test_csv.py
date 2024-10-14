from datetime import datetime
from app.services.transaction_service import TransactionService
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository

# Initialize the repository and service
repo = SQLiteTransactionRepository(":memory:")
service = TransactionService(repo)

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add some sample transactions
service.add_transaction("Grocery Shopping", "Expense", "Food", 150)  # Automatically treated as -150
service.add_transaction("Movie Ticket", "Expense", "Entertainment", 50)  # Automatically treated as -50
service.add_transaction("Salary", "Income", "Job", 1000)  # Treated as 1000

# Export transactions to CSV
service.export_transactions_to_csv("transactions23.csv")
