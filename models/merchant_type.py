# - Defines a spending category via MerchantType i.e this could be "entertainment", "groceries", "general subscription"

class MerchantType:
    
    def __init__(self, name, id=None):
        self.name = name
        self.id = id
