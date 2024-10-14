from flask import Flask

from app.routes.transactions import transactions_bp
from app.routes.budgets import budgets_bp
from app.repositories.SQLiteBudgetRepo import SQLiteBudgetRepository
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository
from app.services.budget_service import BudgetService
from app.services.transaction_service import TransactionService

app = Flask(__name__)

# Create repository instances
budget_repo = SQLiteBudgetRepository("budgets.db")
transaction_repo = SQLiteTransactionRepository("transactions.db")

# Create service instances
transaction_service = TransactionService(transaction_repo)
budget_service = BudgetService(budget_repo, transaction_service)

# Register blueprints
app.register_blueprint(transactions_bp)
app.register_blueprint(budgets_bp)

@app.route("/")
def home():
    return "Welcome to the Personal Finance Tracker"

if __name__ == "__main__":
    app.run(debug=True)
