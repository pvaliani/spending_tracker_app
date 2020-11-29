from db.run_sql import run_sql
from models.amount import Amount
from models.merchant import Merchant
from models.merchant_type import MerchantType
import repositories.merchant_type_repository as merchant_type_repository

def save(merchant):
    sql = "INSERT INTO merchants (name, merchant_type_id) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.merchant_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id


def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for result in results:
        merchant_type = merchant_type_repository.select(result["merchant_type_id"])
        merchant = Merchant(result["name"], merchant_type, result["id"])
        merchants.append(merchant)
    return merchants


def select(id):
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant_type = merchant_type_repository.select(result["merchant_type_id"])
    merchant = Merchant(result["name"], merchant_type, result["id"])
    return merchant


def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(merchant):
    sql = "UPDATE merchants SET (name, merchant_type_id) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.merchant_type.id, merchant.id]
    run_sql(sql, values)

# CHANGE VICTIMS OF ZOMBIE TO ANOTHER NAME AND CROSS REFERENCE OTHER FILES AND VICTIMS VARIABLE - 
def select_recent_spends(id):
    recent_amounts = []
    sql = "SELECT amounts.* FROM amounts INNER JOIN transactions ON transactions.amount_id = amounts.id WHERE transactions.merchant_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        amount = Amount(result["value"])
        recent_amounts.append(amount)
    return recent_amounts