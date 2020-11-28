import unittest
from models.amount import Amount

class TestAmount(unittest.TestCase):
    
    def setUp(self):
        self.amount = Amount(50)
        

    def test_amount_has_a_value(self):
        self.assertEqual(50, self.amount.value)

    def test_amount_has_no_id(self):
        self.amount = Amount(50, None)
        self.assertEqual(None, self.amount.id)
