from abc import ABC, abstractmethod
from app.models.budget import Budget

class BudgetRepository(ABC):
    @abstractmethod
    def add_budget(self, budget: Budget):
        pass

    @abstractmethod
    def get_budgets(self):
        pass
