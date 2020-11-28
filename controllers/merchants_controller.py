from flask import Blueprint, Flask, redirect, render_template, request

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.merchant_type_repository as merchant_type_repository

merchants_blueprint = Blueprint("merchants", __name__)

# INDEX
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants=merchants)
    

# - change from VICTIMS lines 20-24

# SHOW
@merchants_blueprint.route("/merchants/<id>")
def show_merchant(id):
    victims = merchant_repository.select_victims_of_zombie(id)
    merchant = merchant_repository.select(id)
    return render_template("merchants/show.html", victims=victims, merchant=merchant)


# NEW
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    merchant_types = merchant_type_repository.select_all()
    return render_template("merchants/new.html", merchant_types=merchant_types)


# CREATE
@merchants_blueprint.route("/merchants", methods=["POST"])
def create_zombie():
    name = request.form["name"]
    merchant_type_id = request.form["merchant_type_id"]
    merchant_type = merchant_type_repository.select(merchant_type_id)
    new_merchant = Merchant(name, merchant_type)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")


# EDIT
@merchants_blueprint.route("/merchants/<id>/edit")
def edit_zombie(id):
    merchant = merchant_repository.select(id)
    merchant_types = merchant_type_repository.select_all()
    return render_template('merchants/edit.html', merchant=merchant, merchant_types=merchant_types)


# UPDATE
@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_zombie(id):
    name = request.form["name"]
    merchant_type_id = request.form["merchant_type_id"]
    merchant_type = merchant_type_repository.select(merchant_type_id)
    merchant = Merchant(name, merchant_type, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")


# DELETE
@merchants_blueprint.route("/merchants/<id>/delete", methods=["POST"])
def delete_zombie(id):
    merchant_repository.delete(id)
    return redirect("/merchants")
