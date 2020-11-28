import unittest
from models.merchant import Merchant
from models.merchant_type import MerchantType

class TestMerchant(unittest.TestCase):
    
    def setUp(self):
        self.merchant = Merchant("Amazon", "General Purpose")

    def test_merchant_has_a_name(self):
        self.assertEqual("Amazon", self.merchant.name)
    
    def test_merchant_has_a_tag_category(self):
        self.assertEqual("General Purpose", self.merchant.merchant_type)
    