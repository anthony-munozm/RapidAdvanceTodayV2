from flask import Flask, request
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, TEXT, Date
from flask_migrate import Migrate
from config import connection_string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

@app.route('/', methods=['POST', 'GET'])
def short_form_post():

    from models import ShortForm

    if request.method == 'POST': 

        payload = request

        print(payload)

        print("entró en el if del POST")   

        short_form = ShortForm(email="test@gmail.com")

        db.session.merge(short_form)

        db.session.commit()

        return True

    if request.method == 'GET': 

        return "You are using GET invalid method... tony recommends please go back and work using postman and POST"

@app.route('/LongFormStep1', methods=['POST', 'GET'])
def long_form_step1_post():
    if request.method == 'POST': 
        print("entró en el if")     
    return "listo"


@app.route('/LongFormStep2', methods=['POST', 'GET'])
def long_form_step2_post():
    if request.method == 'POST':  
        print("entró en el if")     
    return "listo"


@app.route('/LongFormStep3', methods=['POST', 'GET'])
def long_form_step3_post():
    if request.method == 'POST':  
        print("entró en el if")     
    return "listo"
        

if __name__ == '__main__':
    app.run()