import unittest
from models.user_budget import UserBudget

class TestUserBudget(unittest.TestCase):
    
    def setUp(self):
        self.user_budget = UserBudget(1000)
        
    # - Tests to check various aspects of functionality for the Userbudget class - check amount has a value and no id in the tables when initialised 

    def test_user_budget_has_a_value(self):
        self.assertEqual(1000, self.user_budget.value)

   