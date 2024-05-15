from abc import ABC, abstractmethod
class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, accNo, accType, balance):
        pass
    
    @abstractmethod
    def list_accounts(self):
        pass
    
    @abstractmethod
    def calculate_interest(self):
        pass