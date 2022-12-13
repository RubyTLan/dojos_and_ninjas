from flask_app import app
from flask import Flask, render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninjas")
def add_ninja():
    dojos=Dojo.get_all_dojos()
    return render_template("new_ninja.html",dojos=dojos)

@app.route("/ninjas/create" ,methods=['post'])
def create():
    Ninja.create(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')
