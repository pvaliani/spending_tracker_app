from flask import Blueprint, Flask, redirect, render_template, request

from models.user_budget import UserBudget
import repositories.user_budget_repository as user_budget_repository

user_budgets_blueprint = Blueprint("user_budgets", __name__)

# WORKING

# - first solution working code - UNCOMMENT IF BROKEN W/ DB ******
# user_budget = UserBudget(value=0)

# INDEX - returns a users budget and initialises as 0
@user_budgets_blueprint.route("/userbudgets")
def user_budgets():
    user_budget = user_budget_repository.select()
    return render_template("user_budgets/index.html", new_user_budget=user_budget)

    #ADD BACK IF CODE BROKEN ------
    # return render_template("user_budgets/index.html", new_user_budget=user_budget)

# -----------------------------------

# NEW
@user_budgets_blueprint.route("/userbudgets/new")
def new_user_budget():
    return render_template("user_budgets/new.html")


# CREATE
@user_budgets_blueprint.route("/userbudgets", methods=["POST"])
def create_new_user_budget():
    value = request.form["value"]
    new_value = UserBudget(value)
    user_budget_repository.save(new_value)
    return redirect("/userbudgets")


    # - WORKING CODE FOR ALTERNATIVE CREATE SOLUTION -- UNCOMMENT IF BROKEN *****
    # value = request.form["value"]
    # user_budget.value = value
    # return render_template("/user_budgets/index.html", new_user_budget = user_budget )

# --------------------------------------


# EDIT
@user_budgets_blueprint.route("/userbudgets/edit")
def edit_user_budget():
    user_budget = user_budget_repository.select()
    return render_template('user_budgets/edit.html', user_budget=user_budget)


# UPDATE
@user_budgets_blueprint.route("/userbudgets/update", methods=["POST"])
def update_user_budget():
    value = request.form["value"]
    user_budget = UserBudget(value)
    user_budget_repository.update(user_budget)
    return redirect("/userbudgets")

# ---------------------- MY VER

# # DELETE
# @user_budgets_blueprint.route("/userbudgets/delete", methods=["POST"])
# def delete_user_budget():
#     # delete from here
#     return redirect("/userbudgets")










