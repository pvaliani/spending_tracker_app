import unittest
from models.merchant import Merchant
from models.merchant_type import MerchantType
from models.amount import Amount
from models.transaction import Transaction


class TestTransaction(unittest.TestCase):
    
    def setUp(self):
        self.transaction = Transaction(50, "eBay")

    def test_transaction_has_an_amount(self):
        self.assertEqual(50, self.transaction.amount)

    def test_transaction_has_a_merchant(self):
        self.assertEqual("eBay", self.transaction.merchant)