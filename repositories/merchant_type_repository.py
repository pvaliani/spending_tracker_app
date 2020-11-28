from db.run_sql import run_sql
from models.merchant_type import MerchantType

def save(merchant_type):
    sql = "INSERT INTO merchant_types (name) VALUES (%s) RETURNING id"
    values = [merchant_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant_type.id = id


def select_all():
    merchant_types = []
    sql = "SELECT * FROM merchant_types"
    results = run_sql(sql)
    for result in results:
        merchant_type = MerchantType(result["name"], result["id"])
        merchant_types.append(merchant_type)
    return merchant_types


def select(id):
    sql = "SELECT * FROM merchant_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant_type = MerchantType(result["name"], result["id"])
    return merchant_type


def delete_all():
    sql = "DELETE FROM merchant_types"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM merchant_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(merchant_type):
    sql = "UPDATE merchant_types SET name = %s WHERE id = %s"
    values = [merchant_type.name, merchant_type.id]
    run_sql(sql, values)