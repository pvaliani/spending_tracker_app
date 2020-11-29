# - Import unit test and required classes for testing

import unittest
from models.merchant import Merchant
from models.merchant_type import MerchantType
from models.amount import Amount
from models.transaction import Transaction


class TestTransaction(unittest.TestCase):

     # - Tests to check various aspects of functionality for the Transaction class - check Transaction has an amount, a merchant and no id 
    
    def setUp(self):
        self.transaction = Transaction(50, "eBay")

    def test_transaction_has_an_amount(self):
        self.assertEqual(50, self.transaction.amount)

    def test_transaction_has_a_merchant(self):
        self.assertEqual("eBay", self.transaction.merchant)

    def test_transaction_has_no_id(self):
        self.assertEqual(None, self.transaction.id)