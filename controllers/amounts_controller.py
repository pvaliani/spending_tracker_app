from flask import Blueprint, Flask, redirect, render_template, request

from models.amount import Amount
import repositories.amount_repository as amount_repository

amounts_blueprint = Blueprint("amounts", __name__)

# INDEX
@amounts_blueprint.route("/amounts")
def amounts():
    amounts = amount_repository.select_all()
    return render_template("amounts/index.html", amounts=amounts)


# NEW
@amounts_blueprint.route("/amounts/new")
def new_amount():
    return render_template("amounts/new.html")


# CREATE
@amounts_blueprint.route("/amounts", methods=["POST"])
def create_amount():
    value = request.form["value"]
    new_value = Amount(value)
    amount_repository.save(new_value)
    return redirect("/amounts")


# EDIT
@amounts_blueprint.route("/amounts/<id>/edit")
def edit_amount(id):
    amount = amount_repository.select(id)
    return render_template('amounts/edit.html', amount=amount)


# UPDATE
@amounts_blueprint.route("/amounts/<id>", methods=["POST"])
def update_amount(id):
    value = request.form["value"]
    amount = Amount(value, id)
    amount_repository.update(amount)
    return redirect("/amounts")


# DELETE
@amounts_blueprint.route("/amounts/<id>/delete", methods=["POST"])
def delete_amount(id):
    amount_repository.delete(id)
    return redirect("/amounts")
