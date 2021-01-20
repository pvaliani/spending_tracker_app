from db.run_sql import run_sql
from models.transaction import Transaction
from models.amount import Amount
import repositories.amount_repository as amount_repository
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

# - Save a transaction

def save(transaction):
    sql = "INSERT INTO transactions (amount_id, merchant_id) VALUES (%s, %s) RETURNING id"
    values = [transaction.amount.id, transaction.merchant.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id

# - Set up an empty transactions list to store all transactions
# - Select all from transactions in the PostGreSQL database
# - Initiate SQL runnner
# - For each iteration in the results list of dictionaries
# - An amount is defined by the amount_id selected on each pass of the loop in results

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        amount = amount_repository.select(result["amount_id"])
        merchant = merchant_repository.select(result["merchant_id"])
        transaction = Transaction(amount, merchant, result["id"])
        transactions.append(transaction)
    return transactions


def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    amount = amount_repository.select(result["amount_id"])
    merchant = merchant_repository.select(result["merchant_id"])
    transaction = Transaction(amount, merchant, result["id"])
    return transaction


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(transaction):
    sql = "UPDATE transactions SET (amount_id, merchant_id) = (%s, %s) WHERE id = %s"
    values = [transaction.amount.id, transaction.merchant.id, transaction.id]
    run_sql(sql, values)


# EXTENSION WORK 18/12/2020 ----------------------------------------

def get_total_transactions():
    total = 0
    transactions = select_all()
    for transaction in transactions:
        total += transaction.amount.value
    
    return total

    # Problem is the total is updated in view but when a transaction is deleted the total doesn't update
    # As the amount in the amount table is not deleted -- FIXED
    # now when i delete a transaction it will delete by the amount id whcih means any transactions of the same value will be removed - unwanted behaviour. changed from amount.id to amount.value in get total transactions - REMOVED ON DELETE CASCADE BUT AMMOUNT 2 IS STILL IN REPOSITORY
