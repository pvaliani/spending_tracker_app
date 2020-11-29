import unittest
from models.merchant_type import MerchantType

class TestMerchantType(unittest.TestCase):

    # - Tests to check various aspects of functionality for the MerchantType class - check merchant_type has a name and no id 
    
    def setUp(self):
        self.merchant_type = MerchantType("Entertainment")

    def test_merchant_has_a_type(self):
        self.assertEqual("Entertainment", self.merchant_type.name)

    def test_merchant_has_no_id(self):
        self.assertEqual(None, self.merchant_type.id)