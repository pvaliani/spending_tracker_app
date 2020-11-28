import pdb

# from models.transaction import Transaction
# import repositories.biting_repository as biting_repository

from models.amount import Amount
import repositories.amount_repository as amount_repository

# from models.merchant import Merchant
# import repositories.merchant_repository as merchant_repository

# from models.merchant_type import MerchantType
# import repositories.merchant_type_repository as merchant_type_repository

# Import classes and repositories here ---------------


# transaction_repository.delete_all()
amount_repository.delete_all()
# merchant_repository.delete_all()
# merchant_type_repository.delete_all()



amount_1 = Amount(30)
amount_repository.save(amount_1)

amount_2 = Amount(50)
amount_repository.save(amount_2)