from flask import Flask, render_template

# CONTROLLER BLUEPRINT IMPORTS HERE

from controllers.transactions_controller import transactions_blueprint
from controllers.amounts_controller import amounts_blueprint
from controllers.merchants_controller import merchants_blueprint
from controllers.merchant_types_controller import merchant_types_blueprint


app = Flask(__name__)


# BLUEPRINT REGISTRATION HERE 

app.register_blueprint(transactions_blueprint)
app.register_blueprint(amounts_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(merchant_types_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()