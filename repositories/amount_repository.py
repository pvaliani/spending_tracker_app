from db.run_sql import run_sql
from models.amount import Amount

# - Save a new amount value into amounts table
# - SQL statement to input into table
# - Set the value attribute of amount to a list 
# - run_sql takes a list and returns a list of dictionaries
# - The id of the amount is then the very first position of the results list of dict and it's dict key is id, dict value is the id associated with ['id']

def save(amount):
    sql = "INSERT INTO amounts (value) VALUES (%s) RETURNING id"
    values = [amount.value]
    results = run_sql(sql, values)
    id = results[0]['id']
    amount.id = id

# - SQL: Select all table data from amounts
# - Run the SQL runner method
# - Loop through the results
# - Results is a list of dict. So we define an amount as being the key/value pair at each index of the results list of dict
# - Append each amount into the amounts list and return it so we have all selected items in the database


def select_all():
    amounts = []
    sql = "SELECT * FROM amounts"
    results = run_sql(sql)
    for result in results:
        amount = Amount(result["value"], result["id"])
        amounts.append(amount)
    return amounts

# - SQL = Select all table entries from amounts when presented with an id
# - id has no attributes but is index position 0 in the list of values

def select(id):
    sql = "SELECT * FROM amounts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    amount = Amount(result["value"], result["id"])
    return amount

# - SQL: delete all from the table. Execute SQL runner

def delete_all():
    sql = "DELETE FROM amounts"
    run_sql(sql)

# - SQL: delete the amount from the table when given an id

def delete(id):
    sql = "DELETE FROM amounts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# - SQL: update the amounts tables user spend value where the id is ""
# - run_sql expects a list and returns a list of dict. Therefore provide an amount value and amount id to identify the update required.

def update(amount):
    sql = "UPDATE amounts SET value = %s WHERE id = %s"
    values = [amount.value, amount.id]
    run_sql(sql, values)
