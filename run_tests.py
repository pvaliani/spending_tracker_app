# - Run tests across all project classes to check functionality is correct

import unittest

from tests.amount_test import TestAmount
from tests.merchant_type_test import TestMerchantType
from tests.merchant_test import TestMerchant
from tests.transaction_test import TestTransaction
from tests.user_budget_test import TestUserBudget


if __name__ == '__main__':
    unittest.main()