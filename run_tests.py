import unittest

from models.amount import Amount


# IMPORT all tests from tests folder i.e tests.merchant_test import TestMerchant

from tests.amount_test import TestAmount
from tests.merchant_type_test import TestMerchantType
from tests.merchant_test import TestMerchant
from tests.transaction_test import TestTransaction


if __name__ == '__main__':
    unittest.main()