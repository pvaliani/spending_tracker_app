# - Defines a transaction as having an amount and associated merchant i.e transaction has an amount of £50 spend at Deliveroo

class Transaction:
    
    def __init__(self, amount, merchant, id=None):
        self.amount = amount
        self.merchant = merchant
        self.id = id
