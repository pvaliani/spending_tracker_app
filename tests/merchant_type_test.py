import unittest
from models.merchant_type import MerchantType

class TestMerchantType(unittest.TestCase):
    
    def setUp(self):
        self.merchant_type = MerchantType("Entertainment")

    def test_merchant_has_a_type(self):
        self.assertEqual("Entertainment", self.merchant_type.name)