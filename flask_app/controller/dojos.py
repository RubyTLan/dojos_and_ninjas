from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/dojos/<int:id>')
def dojo_ninjas(id):
    data={
        'id':id
    }
    dojo=Dojo.get_one_with_ninjas(data)
    return render_template("dojo_show.html",dojo=dojo)


@app.route('/dojos/create', methods=['post'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojos')
def display_dojos():
    dojos=Dojo.get_all_dojos()
    return render_template('dojos.html',dojos=dojos)
