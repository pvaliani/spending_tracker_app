from flask import Blueprint, Flask, redirect, render_template, request

from models.user_budget import UserBudget

user_budgets_blueprint = Blueprint("user_budgets", __name__)


# INDEX - returns a users budget and initialises as 0
@user_budgets_blueprint.route("/userbudgets")
def user_budgets():
    user_budget = UserBudget(value=0)
    return render_template("user_budgets/index.html", user_budget=user_budget )


# NEW
@user_budgets_blueprint.route("/userbudgets/new")
def new_user_budget():
    return render_template("user_budgets/new.html")


# CREATE
@user_budgets_blueprint.route("/userbudgets", methods=["POST"])
def create_new_user_budget():
    value = request.form["value"]
    new_user_budget = UserBudget(value)
    return redirect("/userbudgets")


# EDIT
@user_budgets_blueprint.route("/userbudgets/edit")
def edit_user_budget():
    #select sttement
    return render_template('user_budgets/edit.html', user_budget=user_budget)


# UPDATE
@user_budgets_blueprint.route("/userbudgets", methods=["POST"])
def update_user_budget():
    value = request.form["value"]
    user_budget = UserBudget(value)
    # update statement here??


# DELETE
@user_budgets_blueprint.route("/userbudgets/delete", methods=["POST"])
def delete_user_budget():
    # delete from here
    return redirect("/userbudgets")
