from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/create_ninja')
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos = all_dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]   
    }
    Ninja.save(data)
    return redirect('/create_ninja')

@app.route('/go_home')
def go_home():
    return redirect('/')

@app.route('/all_ninjas')
def display_all_ninjas():
    get_all_ninjas = Ninja.all_ninjas()
    ninjas_with_dojos = Ninja.get_ninjas_and_dojos()
    return render_template("all_ninjas.html", ninjas = get_all_ninjas, ninjas_with_dojos=ninjas_with_dojos)