from flask import Blueprint, request, jsonify

from app.services.transaction_service import TransactionService
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository

transactions_bp = Blueprint('transactions', __name__)

# Set up your repository and service instances
transaction_repo = SQLiteTransactionRepository("transactions.db")
transaction_service = TransactionService(transaction_repo)

@transactions_bp.route("/add_transaction", methods=["POST"])
def add_transaction():
    data = request.json
    print(f"Received data: {data}")  # Debugging line
    try:
        transaction_service.add_transaction(data["description"], data["category"], data["subcategory"], data["amount"])
        return jsonify({"message": "Transaction added successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Error: {e}")  # Debugging line
        return jsonify({"error": "An error occurred while adding the transaction."}), 500


@transactions_bp.route("/transactions", methods=["GET"])
def get_transactions():
    transactions = transaction_service.get_transactions()
    return jsonify(transactions), 200

@transactions_bp.route("/export_to_csv", methods=["GET"])
def export_to_csv():
    file_name = "transactions.csv"
    transaction_service.export_transactions_to_csv(file_name)
    return jsonify({"message": f"Transactions exported to {file_name}"}), 200
