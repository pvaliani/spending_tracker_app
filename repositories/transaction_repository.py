from db.run_sql import run_sql
from models.transaction import Transaction
from models.amount import Amount
import repositories.amount_repository as amount_repository
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository



def save(transaction):
    sql = "INSERT INTO transactions (amount_id, merchant_id) VALUES (%s, %s) RETURNING id"
    values = [transaction.amount.id, transaction.merchant.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id


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
