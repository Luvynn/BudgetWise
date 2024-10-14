import pandas as pd
from app.models.budget import Budget
from app.repositories.budgetRepo import BudgetRepository
from app.services.transaction_service import TransactionService
from app.repositories.SQLiteTransactionRepo import SQLiteTransactionRepository

# Adding here for comparison
transaction_repo = SQLiteTransactionRepository("transactions.db")
transaction_service = TransactionService(transaction_repo)

class BudgetService:
    def __init__(self, budget_repo, transaction_service):
        self.budget_repo = budget_repo
        self.transaction_service = transaction_service

    def add_budget(self, category, amount):
        budget = Budget(category, amount)
        self.budget_repo.add_budget(budget)

    def get_budgets(self):
        return self.budget_repo.get_budgets()

    def compare_budget(self):
        transactions = self.transaction_service.get_transactions()
        budgets = self.get_budgets()
        
        spending_by_category = {}
        for transaction in transactions:
            subcategory = transaction[4]  # Using subcategory now
            amount = transaction[5]
            if subcategory in spending_by_category:
                spending_by_category[subcategory] += amount
            else:
                spending_by_category[subcategory] = amount

        comparison = {}
        for budget in budgets:
            category = budget[1]
            budget_amount = budget[2]
            spent = abs(spending_by_category.get(category, 0))
            comparison[category] = {
                "budgeted": budget_amount,
                "spent": spent,
                "remaining": budget_amount - spent
            }

        return comparison
        
    def export_budgets_to_csv(self, file_name='budgets_comparison.csv'):
        comparison = self.compare_budget()
        df = pd.DataFrame([
            {"Category": cat, "Budgeted": data["budgeted"], "Spent": data["spent"], "Remaining": data["remaining"]}
            for cat, data in comparison.items()
        ])
        df.to_csv(file_name, index=False, float_format='%.2f')