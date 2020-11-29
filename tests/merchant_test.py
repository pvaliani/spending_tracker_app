import unittest
from models.merchant import Merchant
from models.merchant_type import MerchantType

class TestMerchant(unittest.TestCase):
    
    def setUp(self):
        self.merchant = Merchant("Amazon", "General Purpose")

    # - Tests to check various aspects of functionality for the Merchant class - check merchant has a name, a tag and no id 

    def test_merchant_has_a_name(self):
        self.assertEqual("Amazon", self.merchant.name)
    
    def test_merchant_has_a_tag_category(self):
        self.assertEqual("General Purpose", self.merchant.merchant_type)

    def test_merchant_has_no_id(self):
        self.merchant= Merchant("Ebay", "Xmas Gifts", None)
        self.assertEqual(None, self.merchant.id)
    