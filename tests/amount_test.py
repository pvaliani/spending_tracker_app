import unittest
from models.amount import Amount

class TestAmount(unittest.TestCase):
    
    def setUp(self):
        self.amount = Amount(50)
        
    # - Tests to check various aspects of functionality for the Amount class - check amount has a value and no id in the tables when initialised 

    def test_amount_has_a_value(self):
        self.assertEqual(50, self.amount.value)

    def test_amount_has_no_id(self):
        self.amount = Amount(50, None)
        self.assertEqual(None, self.amount.id)
