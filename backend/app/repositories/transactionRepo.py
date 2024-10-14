# backend/app/repositories/transactionRepo.py

from abc import ABC, abstractmethod
from app.models.transaction import Transaction

class transactionRepo(ABC):
    @abstractmethod
    def add_transaction(self, transaction: Transaction):
        pass
    
    @abstractmethod
    def get_transactions(self):
        pass
