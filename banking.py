import uuid


class SameAccount(Exception):
    pass


class DifferentBanks(Exception):
    pass


class InsufficientFunds(Exception):
    pass


class Account:
    def __init__(self, bank, id):
        self.bank = bank
        self.id = id

    @property
    def balance(self):
        return self.bank.get_balance(self.id)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.bank == other.bank
            and self.id == other.id
        )


class Bank:
    def __init__(self):
        self.balance=0

    def create_account(self,balance=100):
        self.balance= balance
        return Account(self.__class__,uuid.uuid4())
    
    
    def transfer(self,account1,account2,num):
        if account1 == account2:
            self.balance-=num 
            
    def get_balance(self,id):
        #id (do someting)
        return self.balance




