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
    new_user_budget = UserBudget(value)
    merchant_type_repository.save(new_user_budget)
    return redirect("/userbudgets")


# EDIT
@user_budgets_blueprint.route("/userbudgets/edit")
def edit_merchant_type():
    user_budget = merchant_type_repository.select()
    return render_template('user_budgets/edit.html', user_budget=user_budget)


# UPDATE
@user_budgets_blueprint.route("/userbudgets/<>", methods=["POST"])
def update_merchant():
    value = request.form["value"]
    user_budget = UserBudget(value)
    merchant_type_repository.update(user_budget)


# DELETE
@user_budgets_blueprint.route("/userbudgets/delete", methods=["POST"])
def delete_merchant():
    merchant_type_repository.delete()
    return redirect("/userbudgets")
