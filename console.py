# - Import de-bugging tools, models and repositories

import pdb

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

from models.amount import Amount
import repositories.amount_repository as amount_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.merchant_type import MerchantType
import repositories.merchant_type_repository as merchant_type_repository

from models.user_budget import UserBudget
import repositories.user_budget_repository as user_budget_repository


# - Clear all tables in the project database

transaction_repository.delete_all()
amount_repository.delete_all()
merchant_repository.delete_all()
merchant_type_repository.delete_all()
user_budget_repository.delete_all()

# - Initial data which seeds to database

amount_1 = Amount(33.40)
amount_repository.save(amount_1)

amount_2 = Amount(50.31)
amount_repository.save(amount_2)

amount_3 = Amount(100.50)
amount_repository.save(amount_3)

amount_4 = Amount(1500)
amount_repository.save(amount_4)

merchant_type_1 = MerchantType("Groceries")
merchant_type_repository.save(merchant_type_1)

merchant_type_2 = MerchantType("Entertainment")
merchant_type_repository.save(merchant_type_2)

merchant_type_3 = MerchantType("General Subscription")
merchant_type_repository.save(merchant_type_3)

merchant_1 = Merchant("Amazon", merchant_type_2)
merchant_repository.save(merchant_1)

merchant_2 = Merchant("eBay", merchant_type_1)
merchant_repository.save(merchant_2)

transaction_1 = Transaction(amount_2, merchant_2)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(amount_3, merchant_1)
transaction_repository.save(transaction_2)

transaction_3 = Transaction(amount_3, merchant_2)
transaction_repository.save(transaction_3)

transaction_4 = Transaction(amount_4, merchant_2)
transaction_repository.save(transaction_4)

user_budget = UserBudget(0)
user_budget_repository.save(user_budget)

# - Uncomment the below line to run the de-bugger when implementing and testing new functionality

# pdb.set_trace()