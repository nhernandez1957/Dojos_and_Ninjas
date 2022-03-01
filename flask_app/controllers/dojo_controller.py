from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/')

@app.route('/<int:dojo_id>')
def dojo(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    dojo = Dojo.get_dojo(data)
    return render_template("show_dojo.html", dojo = dojo)