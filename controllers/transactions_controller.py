from flask import Blueprint, Flask, redirect, render_template, request

from models.amount import Amount
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.amount_repository as amount_repository
import repositories.merchant_repository as merchant_repository
import repositories.merchant_type_repository as merchant_type_repository

transactions_blueprint = Blueprint("transactions", __name__)

# INDEX
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
   
    merchant_types = merchant_type_repository.select_all()

    total = amount_repository.sum()
    return render_template("transactions/index.html", transactions=transactions, merchant_types=merchant_types, total=total)


# NEW
@transactions_blueprint.route("/transactions/new")
def new_transaction():
    amounts = amount_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("transactions/new.html", amounts=amounts, merchants=merchants)


# CREATE
@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    amount_value = request.form["amount"]
    amount_obj = Amount(amount_value)
    amount_repository.save(amount_obj)
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    new_transaction = Transaction(amount_obj, merchant)
    transaction_repository.save(new_transaction)
    return redirect("/transactions")


# EDIT
@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    amounts = amount_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template('transactions/edit.html', transaction=transaction, amounts=amounts, merchants=merchants)


# UPDATE
@transactions_blueprint.route("/transactions/<id>", methods=["POST"])
def update_transaction(id):
    amount_value = request.form["amount"]
    amount_obj = Amount(amount_value)
    amount_repository.save(amount_obj)
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount_obj, merchant, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")


# DELETE
@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")
