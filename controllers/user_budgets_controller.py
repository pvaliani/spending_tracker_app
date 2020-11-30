from flask import Blueprint, Flask, redirect, render_template, request

from models.user_budget import UserBudget

user_budgets_blueprint = Blueprint("user_budgets", __name__)


# INDEX
@user_budgets_blueprint.route("/userbudgets")
def user_budgets():
    return render_template("user_budgets/index.html")


# NEW
@user_budgets_blueprint.route("/userbudgets/new")
def new_user_budget():
    return render_template("user_budgets/new.html")


# CREATE
@user_budgets_blueprint.route("/userbudgets", methods=["POST"])
def create_merchant_type():
    value = request.form["value"]
    new_user_budget = MerchantType(value)
    merchant_type_repository.save(new_user_budget)
    return redirect("/userbudgets")


# EDIT
@user_budgets_blueprint.route("/userbudgets/<id>/edit")
def edit_merchant_type(id):
    merchant_type = merchant_type_repository.select(id)
    return render_template('user_budgets/edit.html', merchant_type=merchant_type)


# UPDATE
@user_budgets_blueprint.route("/userbudgets/<id>", methods=["POST"])
def update_merchant(id):
    value = request.form["value"]
    merchant_type = MerchantType(value, id)
    merchant_type_repository.update(merchant_type)


# DELETE
@user_budgets_blueprint.route("/userbudgets/<id>/delete", methods=["POST"])
def delete_merchant(id):
    merchant_type_repository.delete(id)
    return redirect("/userbudgets")
