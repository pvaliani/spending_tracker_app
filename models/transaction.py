class Transaction:
    
    def __init__(self, amount, merchant, id=None):
        self.amount = amount
        self.merchant = merchant
        self.id = id
