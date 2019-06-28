from flask import Flask, request
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, TEXT, Date
from flask_migrate import Migrate
from config import connection_string
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

@app.route('/', methods=['POST', 'GET'])
def short_form_post():

    """from models import ShortForm

    if request.method == 'POST': 

        payload = request

        print(payload)

        print("entró en el if del POST") 

        short_form = ShortForm(email="test@gmail.com", price=1000, last_4_of_ssn=100, birthday=datetime.now(), zip=10141)

        db.session.merge(short_form)

        db.session.commit()

        return True

    if request.method == 'GET': 

        return "You are using GET invalid method... tony recommends please go back and work using postman and POST"""
        
    if request.method == "POST":
        resp = json.dumps(request.form.to_dict(), ensure_ascii=False)
        db.session.merge(resp)
        db.session.commit()
    return render_template('get-started.html')


@app.route('/LongFormStep1', methods=['POST', 'GET'])
def long_form_step1_post():
    if request.method == "POST":
        resp = json.dumps(request.form.to_dict(), ensure_ascii=False)
        db.session.merge(resp)
        db.session.commit()
    return render_template('get-started-2.html')


@app.route('/LongFormStep2', methods=['POST', 'GET'])
def long_form_step2_post():
    if request.method == "POST":
        resp = json.dumps(request.form.to_dict(), ensure_ascii=False)
        db.session.merge(resp)
        db.session.commit()
    return render_template('get-started-3.html')


@app.route('/LongFormStep3', methods=['POST', 'GET'])
def long_form_step3_post():
    if request.method == "POST":
        resp = json.dumps(request.form.to_dict(), ensure_ascii=False)
        db.session.merge(resp)
        db.session.commit()
    return render_template('get-started-3.html')
        

if __name__ == '__main__':
    app.run()