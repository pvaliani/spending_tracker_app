from flask import Blueprint, Flask, redirect, render_template, request

from models.user_budget import UserBudget

user_budgets_blueprint = Blueprint("user_budgets", __name__)