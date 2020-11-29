# - Defines a merchant as having a name i.e "Amazon" and a spending type via merchant_type i.e "General Subscription"

class Merchant:

    def __init__(self, name, merchant_type, id=None):
        self.name = name
        self.merchant_type = merchant_type
        self.id = id
