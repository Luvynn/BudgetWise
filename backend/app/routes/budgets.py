from flask import Blueprint, jsonify, request
from app.services.budget_service import BudgetService
from app.services.transaction_service import TransactionService
from app.repositories.SQLiteBudgetRepo import SQLiteBudgetRepository
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository

budgets_bp = Blueprint('budgets', __name__)

# Initialize repositories and services
budget_repo = SQLiteBudgetRepository("budgets.db")
transaction_repo = SQLiteTransactionRepository("transactions.db")
transaction_service = TransactionService(transaction_repo)
budget_service = BudgetService(budget_repo, transaction_service)

@budgets_bp.route("/add_budget", methods=["POST"])
def add_budget():
    data = request.json
    budget_service.add_budget(data["category"], data["amount"])
    return jsonify({"message": "Budget added successfully"}), 201

@budgets_bp.route("/budgets", methods=["GET"])
def get_budgets():
    budgets = budget_service.get_budgets()
    return jsonify(budgets), 200

@budgets_bp.route("/compare_budget", methods=["GET"])
def compare_budget():
    comparison = budget_service.compare_budget()
    return jsonify(comparison), 200

@budgets_bp.route("/export_budgets_to_csv", methods=["GET"])
def export_budgets_to_csv():
    file_name = "budgets_comparison.csv"
    budget_service.export_budgets_to_csv(file_name)
    return jsonify({"message": f"Budgets exported to {file_name} with comparisons"}), 200