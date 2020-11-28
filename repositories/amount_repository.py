from db.run_sql import run_sql
from models.amount import Amount

def save(amount):
    sql = "INSERT INTO amounts (value) VALUES (%s) RETURNING id"
    values = [amount.value]
    results = run_sql(sql, values)
    id = results[0]['id']
    amount.id = id


def select_all():
    amounts = []
    sql = "SELECT * FROM amounts"
    results = run_sql(sql)
    for result in results:
        amount = Amount(result["value"], result["id"])
        amounts.append(amount)
    return amounts


def select(id):
    sql = "SELECT * FROM amounts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    amount = Amount(result["value"], result["id"])
    return amount


def delete_all():
    sql = "DELETE FROM amounts"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM amounts WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(amount):
    sql = "UPDATE amounts SET value = %s WHERE id = %s"
    values = [amount.value, amount.id]
    run_sql(sql, values)
