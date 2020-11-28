from flask import Flask, render_template

# CONTROLLER BLUEPRINT IMPORTS HERE


app = Flask(__name__)


# BLUEPRINT REGISTRATION HERE 



@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()