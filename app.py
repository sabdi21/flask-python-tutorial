# YOUR FLASK APP HERE
# import modules
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient 
client = MongoClient("mongodb://localhost:27017")
db = client["tutorial"]
# from blueprints.operators import operators_blueprint
# from blueprints.loops import loops_blueprint

#Declare flask app instance
app = Flask(__name__)

# GET	/	Render a home page that includes the Python logo somewhere on the page
#Home Page Route
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/operators')
def operators():
    if request.method == "GET":
        operators = list(db.operators.find())
        return render_template('operators.html', operators=operators)
    else:
        db.operators.insert_one({
            "name": request.form["name"],
            "description": request.form["description"],
            "symbol": request.form["symbol"],
            "example": request.form["example"],
            "uses": request.form["uses"],
        })
        return redirect("/operators")

@app.route('/loops')
def loops():
    return "loops stub"

# require blueprint/controllers
# app.register_blueprint(operators_blueprint)
# app.register_blueprint(loops_blueprint) 

# Listener
if __name__ == "__main__":
    app.run()