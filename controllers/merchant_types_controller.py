from flask import Blueprint, Flask, redirect, render_template, request

from models.merchant_type import MerchantType
import repositories.merchant_type_repository as merchant_type_repository

merchant_types_blueprint = Blueprint("merchant_types", __name__)

# INDEX
@merchant_types_blueprint.route("/merchanttypes")
def merchant_types():
    merchant_types = merchant_type_repository.select_all()
    return render_template("merchant_types/index.html", merchant_types=merchant_types)


# NEW
@merchant_types_blueprint.route("/merchanttypes/new")
def new_merchant_type():
    return render_template("merchant_types/new.html")


# CREATE
@merchant_types_blueprint.route("/merchanttypes", methods=["POST"])
def create_merchant_type():
    name = request.form["name"]
    new_merchant_type = MerchantType(name)
    merchant_type_repository.save(new_merchant_type)
    return redirect("/merchanttypes")


# EDIT
@merchant_types_blueprint.route("/merchanttypes/<id>/edit")
def edit_merchant_type(id):
    merchant_type = merchant_type_repository.select(id)
    return render_template('merchant_types/edit.html', merchant_type=merchant_type)


# UPDATE
@merchant_types_blueprint.route("/merchanttypes/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    merchant_type = MerchantType(name, id)
    merchant_type_repository.update(merchant_type)
    return redirect("/merchanttypes")


# DELETE
@merchant_types_blueprint.route("/merchanttypes/<id>/delete", methods=["POST"])
def delete_merchant(id):
    merchant_type_repository.delete(id)
    return redirect("/merchanttypes")
