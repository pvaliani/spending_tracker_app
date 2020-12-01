from db.run_sql import run_sql
from models.transaction import Transaction
from models.amount import Amount
from models.user_budget import UserBudget
from models.merchant import Merchant

import repositories.amount_repository as amount_repository
import repositories.merchant_repository as merchant_repository

# WORKING
def save(user_budget):
    sql = "INSERT INTO user_budgets (value) VALUES (%s) RETURNING value"
    values = [user_budget.value]
    results = run_sql(sql, values)
    value = results[0]['value']
    user_budget.value = value


def select_all():
    user_budgets = []
    sql = "SELECT * FROM user_budgets"
    results = run_sql(sql)
    for result in results:
        user_budget = UserBudget(result["value"])
        user_budgets.append(user_budget)
    return user_budgets


# - SQL: delete all from the table. Execute SQL runner

def delete_all():
    sql = "DELETE FROM user_budgets"
    run_sql(sql)

# - Possibly update this to say WHERE id = 1?
def update(user_budget):
    sql = "UPDATE user_budgets SET value = %s WHERE id = 1"
    values = [user_budget.value]
    run_sql(sql, values)

